"""
P01.001

Description:

    Floors.

"""
# Import and initialize the pygame library
import pygame
import random
import os
import sys
import json
import pprint

from helper_functions import loadSpriteImages
from helper_functions import loadJson

# Our typical config, but a lot smaller right now.
config = {
    'title' :'P02.001 ',
    'window_size' : (800,800),
    'sprite_sheets':{
        'dude':{'path':'dude_frames'}
    },
    'tile_size':40
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

# Do we extend sprite?
# do we just register a "platform??"
class FloorManager(object):
    """ 
    """
    def __init__(self, **kwargs):

        self.tile_size = kwargs.get('tile_size',25)

        self.platforms = kwargs.get('platforms',None)

        if self.platforms == None:
            print("Error: no platforms to generate!!")
            sys.exit()

        self.platforms = []


class SpriteLoader(object):
    """ Sprite Animation helper to really just load up a json file and turn it into pygame images.
        It has one method: get_animations which returns: 

            {
            'static': [<Surface(80x105x32 SW)>], 
            'down': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>], 
            'right': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>], 
            'left': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>], 
            'up': [<Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>, <Surface(80x105x32 SW)>]
            }

            A dictionary of pre-loaded pygame images. I'm not sure how this would tax the system if we had a ton of assets.
    """
    def __init__(self,**kwargs):
        # get location of sprites for this animation
        self.path = kwargs.get('path',None)

        # if not throw error
        if not self.path:
            print("Error: Need path to location of player_sprites!")
            sys.exit(0)

        self.animation_images = loadSpriteImages(self.path['path'])
        self.size = kwargs.get("resize",None)

          # container for all the pygame images
        self.sprites = {}

        # load images and "convert" them. (see link at top for explanation)
        for anim,imglist in self.animation_images.items():
            self.sprites[anim] = []
            for img in imglist:
                if self.size == None:
                    self.sprites[anim].append(pygame.image.load(img))
                else:
                    im = pygame.image.load(img)
                    frame = pygame.sprite.Sprite()
                    frame.image = pygame.transform.scale(im, (self.size[0], self.size[1]))
                    self.sprites[anim].append(frame.image)

    def get_animations(self):
        return self.sprites  

class ClockManager(object):
    def __init__(self):
        self.ticker = pygame.time.get_ticks()
        self.events = {}
    
    def registerEvent(self,name):
        self.events[name] = pygame.time.get_ticks()

    def checkEvent(self):
        pass

class StateManager(object):
    """ StateManager allows you to register a state (falling, jumping, static, whatever) and then switch between 
        them to help control behaviors.
    """
    def __init__(self,**kwargs):
        """ 
            Params:
                states <list> : a list of states to add
                active <string> : initialize object to this active state
        """
        
        in_states = kwargs.get('in_states',None)
        active = kwargs.get('active',None)

        self.states = {}

        if type(in_states) == list:
            for state in in_states:
                self.states[state] = False
        
        self.active = active
        self.prev = None
        self.history = []
        self.maxHistory = 100000

    def registerState(self,state):
        self.states[state] = False

    def getActiveState(self):
        return self.active

    def setActiveState(self,state):
        if state in self.states:
            self.prev = self.active
            self.active = state
            self.addHistory()
        else:
            print(f"Error: setActiveState({state}) is not a valid state!")
            print(f"Exiting!")
            sys.exit()

    def isActiveState(self,state):
        return state == self.active
    
    def addHistory(self):
        if len(self.history) > self.maxHistory:
            del self.history[0]
        self.history.append((pygame.time.get_ticks(),self.active))

    def dumpHistory(self):
        with open('history_log.log','w') as h:
            for item in self.history:
                h.write(f"Ticks: {item[0]} , State: {item[1]}\n")
    

class HitBox(pygame.sprite.Sprite):
    def __init__(self,**kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.game_width,self.game_height = config['window_size']
        rect = kwargs.get('rect',(0,0,0,0))
        x = kwargs.get('x',0)
        y = kwargs.get('y',0)
        w = kwargs.get('w',0)
        h = kwargs.get('h',0)
        self.buffer = kwargs.get('buffer',10)

        if not rect == None:
            self.box = self.adjustHitBox(rect=rect)
        elif x and y and w and h:
            self.box = self.adjustHitBox(x=x,y=y,w=w,h=h)
        else:
            print("Error: Hitbox needs either a rect(x,y,w,h) or all 4 params seperate.")


    def adjustHitBox(self,**kwargs):
        rect = kwargs.get('rect',None)
        if not rect == None:
            x,y,w,h = rect
        else:
            x = kwargs.get('x',0)
            y = kwargs.get('y',0)
            w = kwargs.get('w',0)
            h = kwargs.get('z',0)

        x = x - self.buffer
        y = y - self.buffer
        
        if x < 0:
            x = 0
        
        if y < 0:
            y = 0
        
        if x + (w + 2*self.buffer) > self.game_width-1:
            w = self.game_width - x
        else:
            w += 2*self.buffer

        # if y + (h + 2*self.buffer) > self.game_height-1:
        #     h = self.game_height - y 
        # else:
        #     h += 2*self.buffer 

        h += self.buffer

        self.image = pygame.Surface([w, h])
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def newHitBox(self,rect):
        if not rect == None:
            self.box = self.adjustHitBox(rect=rect)
        elif x and y and w and h:
            self.box = self.adjustHitBox(x=x,y=y,w=w,h=h)
        else:
            print("Error: Hitbox needs either a rect(x,y,w,h) or all 4 params seperate.")

    def collidesWithRect(self,other):
        return self.box.collidesWith(other)
    
    def collidesWithPoint(self,other):
        return self.box.collidesPoint(other)

class Player(pygame.sprite.Sprite):
    """ Player class the uses an instance of SpriteLoader to load up images.
        Up to now everything is straight forward.
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
        self.state = StateManager(in_states=["grounded", "jumping", "falling"],active="grounded")
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


    def advanceFrame(self):
        """ Get the next frame in the list and update the "rectangle"
        """
        self.currentFrame += 1
        self.image = self.current_animation[self.currentFrame % len(self.current_animation)]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.hitBox = HitBox(rect = self.rect)


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
            print("state: jumping")

        if notMoving:
            self.setAnimation('static')
            self.dy = 0
            self.dx = 0

    def adjustRect(self,key,value):
        """ This method adjusts the "hitbox" in conjunction with 
            the players image.rect 
        """ 
        setattr(self.rect, key, value)
        setattr(self.hitBox.rect, key, value)

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
                print("state: falling")
                self.jumping = False
                self.velocity_current = self.velocity_orig
                self.mass_current = self.mass_orig
                self.gravity_current = 10


    def applyGravity(self):
        """ Add our current gravity to the players y coord.
            Does this need to be a function? Not sure. 
            I was thinking that future versions could have some weird variations...
        """
        self.adjustRect('centery',self.rect.centery + self.gravity_current)

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
            print("new state: grounded")

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
        print(f"{self.state.getActiveState()}")

        
    
def main():
    pygame.init()

    floor_group = None

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    player = Player(path=config['sprite_sheets']['dude'],loc=(config['window_size'][0]//2,config['window_size'][0]//2))
    player = Player(path=config['sprite_sheets']['dude'],loc=(30,800-25),resize=(42,50))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    floor_group = pygame.sprite.Group()

    for row,cols in platforms.items():
        width = cols[1] - cols[0]
        startx = cols[0]
        height = config['tile_size']
        img = pygame.image.load('pink_block.png')
        block = pygame.sprite.Sprite()
        block.image = pygame.transform.scale(img, (width, height))
        block.rect = block.image.get_rect()
        block.rect.x = startx
        block.rect.y = row
        floor_group.add(block)

    # floor = FloorManager(tile_size=10,platforms=platforms,group=floor_group)
    # platforms = floor.getPlatforms()

    # Run until the user asks to quit
    # Basic game loop
    running = True
    while running:

        screen.fill((0,0,0))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())


        platform_collision = pygame.sprite.spritecollide(player.hitBox, floor_group, False)
        
        if platform_collision:
            player.handlePlatformCollision(platform_collision[0])
        
        pygame.draw.rect(screen,(255,0,0),player.rect,2)
        pygame.draw.rect(screen,(0,255,0),player.hitBox.rect,2)

        all_sprites.update()
        all_sprites.draw(screen)

        floor_group.update()
        floor_group.draw(screen)

        pygame.display.flip()


    # Done! Time to quit.
    player.state.dumpHistory()
    pygame.quit()

if __name__=='__main__':
    #colors = fix_colors("colors.json")
    #pprint.pprint(colors)
    main()


