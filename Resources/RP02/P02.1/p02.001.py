"""
P01.001

Description:

    We have basic animations set up. I used a bit of my old code, which I don't know why I didn't want to ?!?
    But I did trim down the number of files in this current project.

"""
# Import and initialize the pygame library
import pygame
import random
import os
import sys
import json

from helper_functions import loadSpriteImages
from helper_functions import loadJson

config = {
    'title' :'P02.001 ',
    'window_size' : (800,800),
    'sprite_sheets':{
        'dude':{'path':'dude_frames'}
    }
}

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

          # container for all the pygame images
        self.sprites = {}

        # load images and "convert" them. (see link at top for explanation)
        for anim,imglist in self.animation_images.items():
            self.sprites[anim] = []
            for img in imglist:
                self.sprites[anim].append(pygame.image.load(img))

    def get_animations(self):
        return self.sprites  


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

        self.width,self.height  = config['window_size']
        self.center             = kwargs.get('loc',(self.width//2,self.height//2))
        self.speed              = kwargs.get('speed',5)
        self.frame_rate         = kwargs.get('frame_rate',50)
        self.dx                 = kwargs.get('dx',0)
        self.dy                 = kwargs.get('dy',0)
        self.gravity            = 5
        self.applyGravity       = True

        # see comment in the SpriteLoader class to see 
        # what got loaded
        self.sprite_sheet = SpriteLoader(path=self.path)

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
            running all four of these commands. 
        """
        self.current_animation = self.animations[key]           # put animation image list into current
        self.current_animation_name = key

        self.image = self.current_animation[self.currentFrame % len(self.current_animation)]  # get a single frame to play                                                              
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def advanceFrame(self):
        self.currentFrame += 1
        self.image = self.current_animation[self.currentFrame % len(self.current_animation)]
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def chooseAnimation(self):     
        keystate = pygame.key.get_pressed()

        notMoving = True

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

        if keystate[pygame.K_SPACE]:
            'space'

        if notMoving:
            self.setAnimation('static')
            self.dy = 0
            self.dx = 0


    def toggleGravity(self):
        # top, left, bottom, right
        # topleft, bottomleft, topright, bottomright
        # midtop, midleft, midbottom, midright
        # center, centerx, centery
        # size, width, height
        # w,h

        # +---------+
        # |         |
        # +---------+

        # if not self.rect.left >= 0 and self.rect.right <= self.width
        #     self.dx *= -1

        print(f"{self.rect.bottom} - {self.height} = {self.rect.bottom - self.height}")

        if abs(self.rect.bottom - self.height) < 5:
            print("we control gravity")
            self.applyGravity = False

            
    def update(self):
        """ Updating players state
        """
        now = pygame.time.get_ticks()

        if now - self.last_update > 50:
            self.advanceFrame()
            self.chooseAnimation()
            self.last_update = now

        if self.applyGravity:
            self.rect.centery += self.gravity

        self.rect.centerx += self.speed * self.dx
        self.center = (self.rect.centerx, self.rect.centery)

        self.toggleGravity()
    


def main():
    pygame.init()


    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    player = Player(path=config['sprite_sheets']['dude'],loc=(config['window_size'][0]//2,config['window_size'][0]//2))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Run until the user asks to quit
    # Basic game loop
    running = True
    while running:

        screen.fill((0,0,0))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    #colors = fix_colors("colors.json")
    #pprint.pprint(colors)
    main()
