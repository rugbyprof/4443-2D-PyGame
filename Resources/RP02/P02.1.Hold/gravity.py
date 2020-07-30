from helper_functions import *
from helper_classes import *

config = loadJson('./resources/config.json')

class Wall(pygame.sprite.Sprite):
    """ Wall:

    """
    def __init__(self, **kwargs):

        # Initiate this sprite
        pygame.sprite.Sprite.__init__(self)
        self.x1 = kwargs.get('x1',None)
        self.y1 = kwargs.get('y1',None)
        self.x2 = kwargs.get('x2',None)
        self.y2 = kwargs.get('y2',None)
        self.width = kwargs.get('width',None)
        self.height = kwargs.get('height',None)

        if None in [self.x1,self.y1,self.x2,self.y2]:
            print("Error: need and x1,y1 and x2,y2 coordinate!")
            sys.exit()

        if None in [self.width,self.height]:
            print("Error: need a width and height!")
            sys.exit()

        self.image = pygame.image.load('./resources/graphics/images/blank_tile.png')

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x1
        self.rect.y = self.y1

    def topOfWall(self,rect):

        if abs(rect.bottom - self.y1) < 2 and self.x1 < rect.right and rect.left < self.x2:
            return True
        return False

    def bottomOfWall(self,y):
        if abs(y - self.y2) < 2:
            return True
        return False


def loadWalls(**kwargs):

    path = kwargs.get('path',None)
    key = kwargs.get('key',None)

    allWalls = pygame.sprite.Group()

    if path == None:
        print("Error: path to 'walls' needs to be a parameter!!")
        sys.exit()

    if key == None:
        print("Error: need json key!")
        sys.exit()

    data = loadJson(path)

    tile_size = data[key]['tile_size']
    walls = data[key]['walls1']

    for rect in walls:
        rect_dict = {}
        rect_dict['x1'] = rect[0] * tile_size
        rect_dict['y1'] = rect[1] * tile_size
        rect_dict['x2'] = rect[2] * tile_size
        rect_dict['y2'] = rect[3] * tile_size
        rect_dict['width'] = abs(rect_dict['x1'] - rect_dict['x2'])
        if rect_dict['y1'] == rect_dict['y2']:
            rect_dict['height'] = tile_size
        else:
            rect_dict['height'] = abs(rect_dict['y1'] - rect_dict['y2'])
        
        wall_sprite = Wall(**rect_dict)
        
        allWalls.add(wall_sprite)

    return allWalls


class Player(PlayerAnimation):
    def __init__(self, **kwargs):
        
        self.gravity_on = True
        self.gravity_force = config['gravity']
        self.jumping = False
        self.m = 1
        self.v = 5

        print(f"force: {self.gravity_force}")

        super().__init__(**kwargs)

    def jump(self):
    
        if self.jumping : 
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
            F =(1 / 2)*self.m*(self.v**2) 

            print(F)
            
            # change in the y co-ordinate 
            self.rect.centery -= F 
            
            # decreasing velocity while going up and become negative while coming down 
            self.v = self.v-1
            
            # object reached its maximum height 
            if self.v<0: 
                
                # negative sign is added to counter negative velocity 
                self.m =-1

            # objected reaches its original state 
            if self.v == -6: 

                # making isjump equal to false  
                self.jumping = False

        
                # setting original values to v and m 
                self.v = 5
                self.m = 1

    def update(self):
        """ Updating players state
        """
        
        if self.jumping:
            self.jump()
        else:
            self.move() # update dx and dy

        old_action = self.action

        # use dx and dy to pick action (direction)
        self.action  = self.choose_animation()

        # if for some reason no action is chosen
        # use the "old action" to choose image with
        if self.action == '':
            self.action = old_action
            center = self.rect.center
            self.image = self.sprites[old_action][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            return

        # if we found an "action" then use it to set image
        self.image = self.sprites[self.action][self.frame]

        now = pygame.time.get_ticks()                           # get current game clock
        
        if now - self.last_update > self.frame_rate:            # has enough time passed to move?   
            self.last_update = now                              # if so reset the clock
            self.frame += 1                                     # get next animation frame
            if self.frame == len(self.sprites[self.action]):    # if at end goto begin ( assembly :) lol)
                self.frame = 0
            else:   
                center = self.rect.center                       # display next frame in animation
                self.image = self.sprites[self.action][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def main():
    pygame.init()
    pressed = None          # which key pressed
    running = True          # game loop runs till told to quit
    mouse_location = None   # holds mouse location if event is fired

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Game size of game window from config
    width = config['window_size']['width']
    height = config['window_size']['height']

    # Set up the drawing window
    screen = pygame.display.set_mode((width,height))

    # load our background
    background = pygame.image.load(config['backgrounds']['gravity_00']['path'])

    # sprite group to handle all the visuals
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    walls_group = loadWalls(path=config['backgrounds']['gravity_00']['walls'],key='gravity_00')
    for wall in walls_group:
        screen.blit(screen,wall.rect)
        all_sprites.add(wall)
   
    # help control event timing
    clock = pygame.time.Clock()

    # load our player
    player = Player(path=config['sprite_sheets']['green_monster']['path'],loc=(400,25),speed=10,dx=1,dy=1)

    # add to player group to help with 
    # interacting with other groups (collisions etc.)
    player_group.add(player)

    # add to all sprites, so we can act upon all
    # sprites at once if necessary.
    all_sprites.add(player)

    # game loop
    while running:

        clock.tick(config['fps'])

        # fill screen with white
        screen.fill(Colors.RGB('lightgray'))

        # show background grid (no moving it)
        screen.blit(background, (0,0),(0,0,width,height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                pressed = event.key

            if event.type == pygame.KEYUP:
                pressed = event.key

            if event.type == pygame.MOUSEMOTION:
                mouse_location = pygame.mouse.get_pos()
                
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_location = pygame.mouse.get_pos()  

        player.gravity_on = True
        for wall in walls_group:
            if wall.topOfWall(player.rect):
                player.gravity_on = False
                break
                

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':

    main()