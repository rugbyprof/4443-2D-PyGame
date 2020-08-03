"""
P02.004

Description:

    Basic platformer with tile loader. 

    Classes: 




"""
# Import and initialize the pygame library
import pygame
import random
import os
import sys
import json
import pprint
# import pytmx
from pytmx.util_pygame import load_pygame 

from helper_functions import loadSpriteImages
from helper_functions import loadJson

# Our typical config, but a lot smaller right now.
config = {
    'title' :'P02.001 ',
    'window_size' : (800,800),
    'sprite_sheets':{
        'dude':{'path':'./resources/dude_frames'}
    },
    'pink_block':"./resources/pink_block.png",
    'tile_size':40,
    'debug': True
}

# Dictionary of platforms, soon to be an 
# imported file with tile information.
platforms = {
    200:[200,600],
    300:[100,400],
    400:[400,800],
    600:[50,600],
    799:[0,800]
}

def debug(statement):
    """ An easy way to globally turn on and off debug statements. Just change config['debug'] to False
    """
    if config['debug']:
        print(statement)

###############################################################################
#   _   _ _ _   ____            
#  | | | (_) |_| __ )  _____  __
#  | |_| | | __|  _ \ / _ \ \/ /
#  |  _  | | |_| |_) | (_) >  < 
#  |_| |_|_|\__|____/ \___/_/\_\
###############################################################################
class HitBox(pygame.sprite.Sprite):
    """ Helps implement a proper hitbox. Where "proper" is a negotiable term. 

    """
    def __init__(self,**kwargs):
        """
            Params:
                rect <tuple> : rectangle tuple

                or

                x <int> : x coord
                y <int> : y coord
                w <int> : width of sprite
                h <int> : height of sprite

                buffer <int> : padding around sprite

                or 

                buffer <tuple> : (left_buffer,top_buffer,right_buffer,bottom_buffer)
        """
        pygame.sprite.Sprite.__init__(self)

        # Get game window size to help with calculations
        self.game_width,self.game_height = config['window_size']
    

        # Get a rect if exists
        self.rect = kwargs.get('rect',None)

        # Otherwise we need all 4 of these 
        self.x = kwargs.get('x',0)
        self.y = kwargs.get('y',0)
        self.w = kwargs.get('w',0)
        self.h = kwargs.get('h',0)

        # buffer defaults to 10px
        self.buffer = kwargs.get('buffer',10)

        # choose which params to build hitbox with
        if not self.rect == None:
            self.box = self.adjustHitBox()
        elif x and y and w and h:
            self.box = self.adjustHitBox()
        else:
            print("Error: Hitbox needs either a rect(x,y,w,h) or all 4 params seperate.")

    def adjustHitBox(self):
        """ This takes the sprite params and widens the hitbox accordingly. You can 
            set each side of the hitbox seperately depending on circumstances. Just pass
            in a buffer tuple like (l,t,r,b) or left, top, right, bottom (clockwise).
            The buffer is passed into the constructor or to the `resetHitBox` method.
                        +--------------+
                        |       t      |
                        |     +---+    |
                        |  l  |   | r  |
                        |     +---+    |
                        |       b      |
                        +--------------+

            The bottom buffer is a little odd in a platformer since we are mostly on the ground. So I
            would recommend setting it to zero.

            Params:
                None
            Returns:
                None
        """

        # if we have a rect passed in the constructor
        if not self.rect == None:
            x,y,w,h = self.rect
        else:
            # get individual values from constructor
            x = self.x
            y = self.y
            w = self.w
            h = self.h

        # if self.buffer is a single integer value add that 
        # to every side of the rectangle
        if type(self.buffer) == int:
            x = x - self.buffer
            y = y - self.buffer
            w = w + 2*self.buffer
            h = h + self.buffer
        else:
            # use the exlicit values in the tuple
            x = x - self.buffer[0]                      # left buffer
            y = y - self.buffer[1]                      # top
            w = w + self.buffer[0] + self.buffer[2]     # width adds left + right buffers
            h = h + self.buffer[1] + self.buffer[3]     # height adds bottom and top

        # adjust if off left screen
        if x < 0:
            x = 0

        # same for top
        if y < 0:
            y = 0

        # same for right
        if x + w > self.game_width:
            w = self.game_width - x

        # same for bottom
        if y + h > self.game_height:
            h = self.game_height - y

        # create a new sprite (so we can use built in collision detection)
        self.image = pygame.Surface([w, h])
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def resetHitBox(self,buffer):
        """ resets the bit box to a different buffer size
            Params:
                buffer <tuple> : (left,top,right,bottom)
            Returns:
                None
        """
        self.buffer = buffer
        self.box = self.adjustHitBox()

###############################################################################
#   ____  _                       
#  |  _ \| | __ _ _   _  ___ _ __ 
#  | |_) | |/ _` | | | |/ _ \ '__|
#  |  __/| | (_| | |_| |  __/ |   
#  |_|   |_|\__,_|\__, |\___|_|   
#                 |___/          
###############################################################################
class Player(pygame.sprite.Sprite):
    """ Player class that represents our platform player. It has the following methods:

        adjustRect(key,value):
            Used to update player location AND it's hitbox. See method for better explanation
        advanceFrame():
            Get the next animation frame for the sprite
        applyGravity():
            A one line function to add to the y coord of the sprite. I made it a function because
            I think future version may have a more complex way of applying gravity.
        chooseAnimation():
            Chooses proper animation based on which keys are pressed and what state the sprite is in.
            Pretty basic right now, but again, I'm looking into the future ... into the year .... 2000! (sorry Conan Obrian joke)
        handlePlatformCollision(platform):
            Game loop sends platorm reference on collision. This method decides what to do. Basically adjusts player position
            based on current state.
        jump():
            You guess.
        movePlayer():
            Based on current state and player location, this method actually updates player position.
        setAnimation(key):
            Choose animation by key (e.g. up, down, left, right)
            This version we only walk up down left right, but future could have: duck, jump, shoot , etc. etc. etc. 
        update()
            The overloaded update method that gets called by the game loop. It does control how fast things happen
            based on the pygame clock. 
    """
    def __init__(self, **kwargs):

        # Initialize parent
        pygame.sprite.Sprite.__init__(self)

        # get location of sprites for this animation
        self.path = kwargs.get('path',None)

        # if not throw error
        if not self.path:
            print("Error: Need path to location of player_sprites!")
            sys.exit(0)

        self.game_width,self.game_height  = config['window_size']
        self.center             = kwargs.get('loc',(self.game_width//2,self.game_height//2))
        self.speed              = kwargs.get('speed',5)
        self.frame_rate         = kwargs.get('frame_rate',50)
        self.dx                 = kwargs.get('dx',0)
        self.dy                 = kwargs.get('dy',0)
        self.resize             = kwargs.get('resize',None)
        self.gravity_current    = 5
        self.gravity_orig       = 5
        self.jumping            = False
        self.jumpCount          = 0
        self.mass_orig          = 2
        self.mass_current       = 2
        self.velocity_orig      = 8
        self.velocity_current   = 8
        self.tired              =.99
        self.current_platform   = None
        self.state = StateManager(states=["grounded", "jumping", "falling"],active="grounded")
        self.hitBox = None

        # see comment in the SpriteLoader class to see 
        # what got loaded
        self.sprite_sheet = SpriteLoader(path=self.path,resize=self.resize)

        # animations = 'key':[list of pygame surface objects]
        self.animations = self.sprite_sheet.get_animations()

        # Holds current animation name (up down left right static)
        self.current_animation = None
        self.current_animation_name = None
        self.currentFrame = 0

        # hmmm whats this do?
        self.setAnimation('static')

        # in case we need to time some things
        self.last_update = pygame.time.get_ticks()

    def adjustRect(self,key,value):
        """ This method adjusts the "hitbox" in conjunction with 
            the players image.rect 
        """ 
        setattr(self.rect, key, value)
        setattr(self.hitBox.rect, key, value)

    def advanceFrame(self):
        """ Get the next frame in the list and update the "rectangle"
        """
        self.currentFrame += 1
        self.image = self.current_animation[self.currentFrame % len(self.current_animation)]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.hitBox = HitBox(rect = self.rect)

    def applyGravity(self):
        """ Add our current gravity to the players y coord.
            Does this need to be a function? Not sure. 
            I was thinking that future versions could have some weird variations...
        """
        self.adjustRect('centery',self.rect.centery + self.gravity_current)

    def chooseAnimation(self):
        """ This a "move" and "animation" method. Based on which keys are pressed
            choose an animation and update player state.
        """

        # get current pygame clock val
        now = pygame.time.get_ticks()

        # get key pressed :)
        keystate = pygame.key.get_pressed()

        # assume no key pressed
        notMoving = True

        # The following check: up down left right where 
        # up/down are kind of ignored (for now cause its a basic 
        # platform scroller. 
        if keystate[pygame.K_UP]:
            self.setAnimation('up')
            #self.dy = -1
            notMoving = False

        if keystate[pygame.K_DOWN]:
            self.setAnimation('down')
            #self.dy = 1
            notMoving = False

        if keystate[pygame.K_LEFT]:
            self.setAnimation('left')
            self.dx = -1
            notMoving = False

        if keystate[pygame.K_RIGHT]:
            self.setAnimation('right')
            self.dx = 1
            notMoving = False

        # Space bar = jump ... but we need to control 
        # how many times you can jump
        if keystate[pygame.K_SPACE]:
            # if now - self.last_update > 250: 
            self.last_update = now
            self.jumping = True
            self.state.setActiveState("jumping")
            debug("state: jumping")

        if notMoving:
            self.setAnimation('static')
            self.dy = 0
            self.dx = 0

    def handlePlatformCollision(self,platform):
        """ Did we contact a platform?
            Parameters:
                platform <pygame.sprite> : a platorm sprite with a rectangle info
        """

        # If were on some ground, adjust our feet to be at proper height
        if self.state.isActiveState("grounded"):
            self.adjustRect('bottom',platform.rect.top)

        # If we are jumping, adjust our top to the platforms bottom because
        # we hit the bottom of a platform! Don't go through it!
        if self.state.isActiveState("jumping"):
            self.adjustRect('top',platform.rect.bottom)

        # If we are falling put our feet on the platform we hit.
        # set our new floor to the current platform and some
        # other stuff ... 
        if self.state.isActiveState("falling"):
            self.adjustRect('bottom',platform.rect.top) # adjust rect and hitbox
            self.state.setActiveState("grounded")
            self.current_platform = platform
            debug("new state: grounded")

    def jump(self):
        """ jump jump ... jump around
        """
        # If we triggered the jump variable
        if self.jumping:
            
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
            F = ((1/2) * self.mass_current * (self.velocity_current**2)) * self.tired
        
            # change in the y co-ordinate 
            #self.rect.centery -= F 
            self.adjustRect('centery',self.rect.centery - F)
            
            # decreasing velocity while going up and become negative while coming down 
            self.velocity_current = self.velocity_current-1
            
            # object reached its maximum height 
            if self.velocity_current<0: 
                self.state.setActiveState("falling")
                debug("state: falling")
                self.jumping = False
                self.velocity_current = self.velocity_orig
                self.mass_current = self.mass_orig
                self.gravity_current = 10

    def movePlayer(self):
        """ First checks to see what "state" its in to apply certain things (like gravity) and 
            then it actually adjusts the players "rectangle" on the game screen by moving its
            center left and right. 
        """

        # if jumping is true run jump function
        if self.jumping:
            self.jump()

        # if player falling, then apply gravity to move player down
        if self.state.isActiveState('falling'):
            self.applyGravity()

        # move player as long as its on the world
        if self.rect.right <= self.game_width and self.rect.left >= 0:
            # Adjust players rect and hiboxes rectangle
            self.adjustRect('centerx',self.rect.centerx + self.speed * self.dx)

            # Comment this out and see what happens
            self.center = (self.rect.centerx, self.rect.centery)
        
        # If your on the edge, you could get stuck. So I made it 
        # so you always get pushed away by one pixel.
        if self.rect.left <= 0:
            self.rect.left = 1
        if self.rect.right >= self.game_width:
            self.rect.right = self.game_width - 1

        # Our current "floor" or "ground"
        if self.current_platform:

            # if we go off the left edge ... fall
            if self.rect.right < self.current_platform.rect.left:
                self.state.setActiveState("falling")

            # same on other side
            if self.rect.left > self.current_platform.rect.right:
                self.state.setActiveState("falling")


    def setAnimation(self,key):
        """ I turned this into a function since everytime the animation is changed I end up
            running all five of these commands. 
        """
        self.current_animation = self.animations[key]           # put animation image list into current
        self.current_animation_name = key

        self.image = self.current_animation[self.currentFrame % len(self.current_animation)]  # get a single frame to play                                                              
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.hitBox = HitBox(rect = self.rect)


    def update(self):
        """ Updating players state
        """
        now = pygame.time.get_ticks()   

        # This keeps the animation at a little slower speed
        # than the rest of the game. Set 50 to 0 and see the difference.
        if now - self.last_update > 100:
            self.advanceFrame()
            self.chooseAnimation()
            self.last_update = now

        self.movePlayer()
        debug(f"{self.state.getActiveState()}")

###############################################################################
#   ____             _ _       _                    _           
#  / ___| _ __  _ __(_) |_ ___| |    ___   __ _  __| | ___ _ __ 
#  \___ \| '_ \| '__| | __/ _ \ |   / _ \ / _` |/ _` |/ _ \ '__|
#   ___) | |_) | |  | | ||  __/ |__| (_) | (_| | (_| |  __/ |   
#  |____/| .__/|_|  |_|\__\___|_____\___/ \__,_|\__,_|\___|_|   
#        |_|                                                   
###############################################################################
class SpriteLoader(object):
    """ Sprite Animation helper to really just load up a json file and turn it into pygame images.
        It has one method: get_animations which returns a dictionary of pre-loaded pygame images: 

            {
            'static': [<Surface(80x105x32 SW)>], 
            'down': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>], 
            'right': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>], 
            'left': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>], 
            'up': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>]
            }

             I'm not sure how this would tax the system if we had a ton of assets, but oh well. 

    """
    def __init__(self,**kwargs):
        """
        Params:
            path <string> : Path to your sprite images
            size <tuple>  : New size for your sprite frames - (new_width,new_height)
        """
        # get location of sprites for this animation
        self.path = kwargs.get('path',None)

        # if not throw error
        if not self.path:
            print("Error: Need path to location of player_sprites!")
            sys.exit(0)

        # Load the images for our sprite
        self.animation_images = loadSpriteImages(self.path['path'])

        # get a new size if one is passed in
        self.size = kwargs.get("resize",None)

        # container for all the pygame images
        self.sprites = {}

        # load images and "convert" them. (see link at top for explanation)
        for anim,imglist in self.animation_images.items():
            self.sprites[anim] = []
            for img in imglist:
                # no size passed in, so just create sprites
                if self.size == None:
                    self.sprites[anim].append(pygame.image.load(img))
                else:
                    # load a resize image by scaling them
                    im = pygame.image.load(img)
                    frame = pygame.sprite.Sprite()
                    frame.image = pygame.transform.scale(im, (self.size[0], self.size[1]))
                    self.sprites[anim].append(frame.image)

    def get_animations(self):
        """ returns the dictionary of animations
        """
        return self.sprites  

###############################################################################
#   ____  _        _       __  __                                   
#  / ___|| |_ __ _| |_ ___|  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
#  \___ \| __/ _` | __/ _ \ |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
#   ___) | || (_| | ||  __/ |  | | (_| | | | | (_| | (_| |  __/ |   
#  |____/ \__\__,_|\__\___|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
#                                                   |___/         
###############################################################################
class StateManager(object):
    """ StateManager allows you to register a state (falling, jumping, static, whatever) and then switch between 
        them to help control behaviors. 
        
        This may be overkill, but I thought in the big picture it could help with game decisions. For example:
            CurrentState: Falling 
            Event: player pushes the left arrow
            Result: don't update postion, player is ... falling

        I know we had some semblence of this in our player class, but again I may have over engineered this one. 
        BUT! Debugging has been harder than we are used to. I also wrote this class as a type of "debug" helper. 
        It logs every state change with the pygame clock. In real life, we could enhance this to find bugs in our
        code! 

        Also, it reads better in the player class!

        Methods:
            addHistory()
                Adds last state change to history
            dumpHistory(filename=None)
                Prints history to a file
            getActiveState()
                Returns the current active state
            isActiveState(state)
                Tests if "state" is the active one
            registerState(state)
                Adds a new state to valid states
            setActiveState(state)
                Sets the new active state and moves current active to previous
    """
    def __init__(self,**kwargs):
        """ 
            Params:
                states <list> : a list of states to add
                active <string> : initialize object to this active state
        """

        states = kwargs.get('states',[])
        active = kwargs.get('active',None)

        self.states = states
        
        self.active = active
        self.prev = None
        self.history = []
        self.maxHistory = 100000


    def addHistory(self):
        """ adds last state change to history
            Params:
                None
            Returns:
                None
        """
        if len(self.history) > self.maxHistory:
            del self.history[0]
        self.history.append((pygame.time.get_ticks(),self.active))


    def dumpHistory(self,filename=None):
        """ writes history to a file
            Params:
                filename <string> : file to write to
            Returns:
                None
        """
        if not filename:
            filename = 'history_log.log'

        with open(filename,'w') as h:
            for item in self.history:
                h.write(f"Ticks: {item[0]} , State: {item[1]}\n")


    def getActiveState(self):
        """ returns current active state
            Params:
                None
            Returns:
                string
        """
        return self.active


    def isActiveState(self,state):
        """ is state the active one?
            Params:
                state <string> : state name
            Returns:
                bool
        """
        return state == self.active


    def registerState(self,state):
        """ Add a new state to the state manager
            Params:
                state <string> : name of state to add
            Returns:
                None
        """
        self.states.append(state)


    def setActiveState(self,state):
        """ sets the active state
            Params:
                state <string> : new active state
            Returns:
                None
        """
        # make sure its a valid state name 
        if state in self.states:
            self.prev = self.active     # active copied to prev
            self.active = state         # new active state
            self.addHistory()           # add these to the history
        else:
            print(f"Error: setActiveState({state}) is not a valid state!")
            print(f"Exiting!")
            sys.exit()
    
###############################################################################
#   _ __ ___   __ _(_)_ __  
#  | '_ ` _ \ / _` | | '_ \ 
#  | | | | | | (_| | | | | |
#  |_| |_| |_|\__,_|_|_| |_|
###############################################################################          
def main():
    pygame.init()

    #tmxdata = pytmx.TiledMap("./resources/map_data/forest_map_level_01.tmx")
    gameMap = load_pygame("./resources/map_data/forest_map_level_01.tmx")

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    # Create our player putting him in bottom left of screen and resizing his sprite
    # from 80x105 to 42x50
    # If you want to maintain aspect ratio when resizing sprites, just divide one side
    # into the other, then use that ratio to create your new size. 
    # e.g. 80/105 = .76 so I multiplied the height (Y value) I wanted: 50 by .76 to get my (X value) 38
    player = Player(path=config['sprite_sheets']['dude'],loc=(30,800-25),resize=(38,50))

    # Sprite groups is the easiest way to update and draw many sprites
    all_sprites = pygame.sprite.Group()

    # Add player to all sprites
    all_sprites.add(player)

    # Floor group will be used to test for collisions
    # between player and platforms
    floor_group = pygame.sprite.Group()

    for row,cols in platforms.items():
        width = cols[1] - cols[0]
        startx = cols[0]
        height = config['tile_size']
        img = pygame.image.load(config['pink_block'])
        block = pygame.sprite.Sprite()
        block.image = pygame.transform.scale(img, (width, height))
        block.rect = block.image.get_rect()
        block.rect.x = startx
        block.rect.y = row
        floor_group.add(block)  # add to floor group for collisions
        all_sprites.add(block)  # add to all_sprites for drawing and updating 


    # Run until the user asks to quit
    # Basic game loop
    running = True
    while running:

        screen.fill((0,0,0))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Not used in this instance of our game
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())

        # check for collisions using our floor_group and players hitbox
        platform_collision = pygame.sprite.spritecollide(player.hitBox, floor_group, False)
        
        # if player collides with platform, tell the player class
        if platform_collision:
            player.handlePlatformCollision(platform_collision[0])
        
        # print out hitbox and bounding rectangle of player
        if config['debug']:
            pygame.draw.rect(screen,(255,0,0),player.rect,1)
            pygame.draw.rect(screen,(0,255,0),player.hitBox.rect,1)

        # These methods will call the "update" method for every sprite that needs it. For example, if 
        # our platforms "moved", then we would need to put an update method in a platform class to 
        # handle it. Right now, they're sprites, but just sit there.
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()


    # Done! Time to quit.
    player.state.dumpHistory()
    pygame.quit()

if __name__=='__main__':

    main()


