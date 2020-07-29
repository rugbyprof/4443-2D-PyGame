""" Helper module stores common functions and config information
    Banners generated with: http://patorjk.com/software/taag/
    Everything is in here right now. 
"""
# Import and initialize the pygame library
import pygame
import random
import json
import pprint
import sys
import os
import math
import glob

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

################################################################################################################
################################################################################################################

 ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ 
██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ 
██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝

# Keep up with the config stuff. Adding sprite sheets for
# characters and other graphics now


################################################################################################################
################################################################################################################

██╗      ██████╗  █████╗ ██████╗      ██╗███████╗ ██████╗ ███╗   ██╗
██║     ██╔═══██╗██╔══██╗██╔══██╗     ██║██╔════╝██╔═══██╗████╗  ██║
██║     ██║   ██║███████║██║  ██║     ██║███████╗██║   ██║██╔██╗ ██║
██║     ██║   ██║██╔══██║██║  ██║██   ██║╚════██║██║   ██║██║╚██╗██║
███████╗╚██████╔╝██║  ██║██████╔╝╚█████╔╝███████║╚██████╔╝██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝

def loadJson(path,filetype):
    """ load a json file for whatever you need!
    """
    if not os.path.isdir(path):
        print(f"Error: {path} not a valid folder!")
        sys.exit()

    if not os.path.isfile(os.path.join(path,filetype)):
        print(f"Error: {filetype} is required to be in folder!")
        sys.exit()

    # open the json file thats expected to be in the folder
    # and read it in as a string
    f = open(os.path.join(path,filetype),"r")

    # make raw string into a python dictionary 
    data = json.loads(f.read())

    return data

################################################################################################################
################################################################################################################

██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ ██████╗ ██╗████████╗███████╗███████╗
██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝██╔════╝
██║     ██║   ██║███████║██║  ██║███████╗██████╔╝██████╔╝██║   ██║   █████╗  ███████╗
██║     ██║   ██║██╔══██║██║  ██║╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  ╚════██║
███████╗╚██████╔╝██║  ██║██████╔╝███████║██║     ██║  ██║██║   ██║   ███████╗███████║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚══════╝                                                                                                                           
                                                              
def  loadSpriteImages(path):
    """ Load sprite images into either a dictionary of moves or a list of images depending
        on whether the "sprite" is a multi move character or a single effect with just frames
        to play.

        This method reads a json file looking for the following formats (right now):

    """

    if not os.path.isfile(os.path.join(path,"moves.json")):
        print(f"Error: 'moves.json' is required to be in folder: {path}!")
        sys.exit()

    # make raw string into a python dictionary 
    sprite_info = loadJson(path,"moves.json")

    # base name is used to build filename
    base_name = sprite_info['base_name']
    # ext as well
    ext = sprite_info['ext']

    # If moves is a key in the dictionary then we create a dictionary of
    # of moves where each move points to a list of images for that move
    if 'moves' in sprite_info:
        moves = {}

        for move,nums in sprite_info['moves'].items():
            moves[move] = []
            for num in nums:
                moves[move].append(os.path.join(path,base_name+num+ext))
        
        return moves

    # If frames in the dictionary, then its an effect with a list of images
    # for that effect. We need to order them before return since glob
    # doesn't get directory items in order. 
    elif 'frames' in sprite_info:
        images = sprite_info['frames']
        
        if type(images) == list:
            pass
        elif type(images) == str and images == '*':
            images = glob.glob(os.path.join(path,'*'+ext))
            images.sort()
            return images

    else:
        print(f"Error: 'moves' or 'frames' key not in json!!")
        sys.exit()

################################################################################################################
################################################################################################################

██████╗ ██╗███████╗████████╗ █████╗ ███╗   ██╗ ██████╗███████╗
██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔════╝
██║  ██║██║███████╗   ██║   ███████║██╔██╗ ██║██║     █████╗  
██║  ██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║██║     ██╔══╝  
██████╔╝██║███████║   ██║   ██║  ██║██║ ╚████║╚██████╗███████╗
╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                                              

def straightDistance(A,B,C=None,D=None):
    '''
    Returns the cartisian distance between 2 points on a 2d plane.

            Parameters:
                    A (int): x coord of point 1
                    B (int): y coord of point 1
                    C (int): x coord of point 2
                    D (int): y coord of point 2

            Returns:
                    distance (float): Cartesian distance
    '''
    if type(A) == tuple and type(B) == tuple:
        distance = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5
    else:
        distance = ((A-C)**2 + (B-D)**2)**0.5
    return distance

def taxiCabDistance(xA,yA,xB,yB):
    '''
    Returns the manhatten or taxi_cab distance between 2 points on a 2d grid.

            Parameters:
                    x1 (int): x coord of point 1
                    y1 (int): y coord of point 1
                    x2 (int): x coord of point 2
                    y2 (int): y coord of point 2

            Returns:
                    distance (float): Manhatten or taxicab  distance
    '''
    distance = abs(xA-xB) + abs(yA-yB)
    return distance

################################################################################################################
################################################################################################################

███╗   ███╗██╗   ██╗     ██╗  ██╗██╗    ██╗ █████╗ ██████╗  ██████╗ ███████╗
████╗ ████║╚██╗ ██╔╝     ██║ ██╔╝██║    ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
██╔████╔██║ ╚████╔╝█████╗█████╔╝ ██║ █╗ ██║███████║██████╔╝██║  ███╗███████╗
██║╚██╔╝██║  ╚██╔╝ ╚════╝██╔═██╗ ██║███╗██║██╔══██║██╔══██╗██║   ██║╚════██║
██║ ╚═╝ ██║   ██║        ██║  ██╗╚███╔███╔╝██║  ██║██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝   ╚═╝        ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                            

def myKwargs(argv):
    '''
    Processes argv list into plain args and kwargs.
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

################################################################################################################
################################################################################################################
 ██████╗ ██████╗ ██╗      ██████╗ ██████╗     ███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗    ██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝
██║     ██║   ██║██║     ██║   ██║██████╔╝    █████╗  ██║   ██║██╔██╗ ██║██║     ███████╗
██║     ██║   ██║██║     ██║   ██║██╔══██╗    ██╔══╝  ██║   ██║██║╚██╗██║██║     ╚════██║
╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║    ██║     ╚██████╔╝██║ ╚████║╚██████╗███████║
 ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝

def loadColors(infile):
    '''
    Loads a json color file into a python dictionary.
        Params:
            infile (string) : path to json input file
        Returns:
            colors (dictionary) : dictionary of colors (hex and rgb)
    '''
    with open(infile,'r') as f:
        data = f.read()
        colors = json.loads(data)
    return colors

def rgbColors(infile):
    '''
    Loads a json color file into a python dictionary.
        Params:
            infile (string) : path to json input file
        Returns:
            colors (dictionary) : dictionary of colors (rgb only)
    '''
    rgb = {}
    with open(infile,'r') as f:
        data = f.read()
        colors = json.loads(data)
    for key,color in colors.items():
        rgb[key] = color['rgb']
    return rgb

################################################################################################################
################################################################################################################

cardinal_directions = ('W','NW','N','NE','E','SE','S','SW')

def getCardinalDirection(origin,target):
    """
    https://gamedev.stackexchange.com/questions/49290/whats-the-best-way-of-transforming-a-2d-vector-into-the-closest-8-way-compass-d

    This method finds the angle between an origin location and a target location.
    Using some simple but cool arithmetic, it converts the angle into an int value: 0-7 (8 values) that corresponds
        to one of the 8 semi-major cardinal directions. Major being N, S, E, and W. Each of the 8 represents a 45 degree
        pie slice of the compass circle.
            Params:
                origin: (tuple): (x,y)
                target: (tuple): (x,y)
            Returns:
                cardinal_direction (string) : one of 'W','NW','N','NE','E','SE','S','SW'
    """
    cards = []
    dx = origin[0] - target[0]
    dy = origin[1] - target[1]
    angle = math.atan2(dy, dx)

    octant = round(8 * angle / (2*math.pi) + 8) % 8

    return cardinal_directions[octant]


#####################################################################################################################
#####################################################################################################################

███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗██║██╔████╔██║██████╔╝██║     █████╗  ███████║██╔██╗ ██║██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                     

class SimpleAnimation(pygame.sprite.Sprite):
    """ Animation:
            This class will run a basic animation for you. 
        Params:
            path <string>   : path to folder of images
            loc <tuple>     : location to place animation
            loop <bool>     : keep running animation?
    """
    def __init__(self, **kwargs):

        # Initiate this sprite
        pygame.sprite.Sprite.__init__(self)

        # get location of sprites for this animation
        path = kwargs.get('path',None)

        # if not throw error
        if not path:
            print("Error: Need location of path!")
            sys.exit(0)

        self.center = kwargs.get('loc',(0,0))

        # Does this animation keep looping?
        self.loop = kwargs.get('loop',False)

        # This function finds the json file and loads all the 
        # image names into a list
        self.images = LoadSpriteImages(path)

        # container for all the pygame images
        self.frames = []

        # load images and "convert" them. (see link at top for explanation)
        for image in self.images:
            self.frames.append(pygame.image.load(image))

        # animation variables
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50                        # smaller = faster

        # prime the animation
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.center 

    def setLocation(self,loc):
        """ Set the center of the explosion
        """
        self.center = loc
        self.rect.center = loc
    
    def update(self):
        """ Overloaded method from sprite which gets called by the game loop when 
            a sprite group gets updated
        """
        now = pygame.time.get_ticks()                   # get current game clock
        if now - self.last_update > self.frame_rate:    
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.frames):
                if not self.loop:
                    self.kill()
                else:
                    self.frame = 0
            else:
                center = self.rect.center
                self.image = self.frames[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

#######################################################################################################################
#######################################################################################################################

██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗  █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████║██╔██╗ ██║██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                     

class PlayerAnimation(pygame.sprite.Sprite):
    def __init__(self, **kwargs):

        # get location of sprites for this animation
        self.path = kwargs.get('path',None)

        # if not throw error
        if not self.path:
            print("Error: Need path to location of player_sprites!")
            sys.exit(0)

        self.center = kwargs.get('loc',(0,0))
        self.speed = kwargs.get('speed',3)
        self.frame_rate = kwargs.get('frame_rate',50)
        self.dx = kwargs.get('dx',random.choice([-1,0,1]))
        self.dy = kwargs.get('dy',random.choice([-1,0,1]))


        # This function finds the json file and loads all the 
        # image names into a list
        self.animation_images = loadSpriteImages(self.path)

        # container for all the pygame images
        self.sprites = {}

        # load images and "convert" them. (see link at top for explanation)
        for anim,imglist in self.animation_images.items():
            self.sprites[anim] = []
            for img in imglist:
                self.sprites[anim].append(pygame.image.load(img))

        # animation variables
        self.animations = list(self.sprites.keys())

        self.frame = 0
        self.action = 'stationary'
        self.last_update = pygame.time.get_ticks()          
   
        # prime the animation
        self.image = self.sprites[self.action][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = self.center 

        # Initiate this sprite
        pygame.sprite.Sprite.__init__(self)

    def move(self):

        keystate = pygame.key.get_pressed()
        self.dx = 0
        self.dy = 0
        if keystate[pygame.K_UP]:
            self.dy = -1

        if keystate[pygame.K_DOWN]:
            self.dy = 1

        if keystate[pygame.K_LEFT]:
            self.dx = -1

        if keystate[pygame.K_RIGHT]:
            self.dx = 1

        if keystate[pygame.K_SPACE]:
            #self.shoot()
            pass

        x = self.rect.centerx + (self.speed * self.dx)
        y = self.rect.centery + (self.speed * self.dy)

        self.rect.center = (x,y)

    def choose_animation(self):
        """ This function assumes at least "up","down","left","right"
            but can handle two keys being pressed. 
            Possible moves:
                up
                down
                left
                right
                upleft
                upright
                downleft
                downright
            The "moves.json" file in an animation folder should have 
            moves named this way.
        """
        action = ''
        
        if self.dy == -1:
            action += 'up'

        if self.dy == 1:
            action += 'down'

        if self.dx == -1:
            action += 'left'

        if self.dx == 1:
            action += 'right'

        if action == '':
            action = 'stationary'
        return action


    def update(self):
        """ Updating players state
        """
        
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

################################################################################################################
################################################################################################################

██╗      ██████╗  ██████╗  ██████╗ 
██║     ██╔═══██╗██╔════╝ ██╔════╝ 
██║     ██║   ██║██║  ███╗██║  ███╗
██║     ██║   ██║██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ 

class Logg:
    """
    Simple little logger clas to help with debugging
    """
    def __init__(self):
        self.logfile = open("logger.txt","w")

    def log(self,stuff):
        self.logfile.write(stuff+"\n")

################################################################################################################
################################################################################################################

███████╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗ ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝██╔══██╗
█████╗  ██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║     ██║   ██║██╔██╗ ██║   ██║   ███████║██║██╔██╗ ██║█████╗  ██████╔╝
██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗
███████╗ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║██║██║ ╚████║███████╗██║  ██║
╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                     

class EventContainer:
    """ Dictionary of events all kept in one place for use in other classes.
        Not sure on "best practices" or performance, but this lets me pass
        all the events to any class or function that needs em.
    """
    def __init__(self):
        self.events = {
            'keydown':None,
            'keyup':None,
            'mouse_motion':None,
            'mouse_button_up':None,
            'all_pressed':None
        }

    def reset(self):
        """ Set all to None
        """
        for k,v in self.events.items():
            self.events[k] = None

    def __str__(self):
        """Dump instance to screen or wherever
        """
        s = ''
        for k,v in self.events.items():
            if k == 'all_pressed':
                continue
            s += f"{k} : {v}\n"

        return s

################################################################################################################
################################################################################################################

 ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝
██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗██║  ██║██║██║        ██║   
██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║██║  ██║██║██║        ██║   
╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║██████╔╝██║╚██████╗   ██║   
 ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝   

colorsDict = {
    "aliceblue": {
        "hex": "#f0f8ff",
        "rgb": [
            240,
            248,
            255
        ]
    },
    "antiquewhite": {
        "hex": "#faebd7",
        "rgb": [
            250,
            235,
            215
        ]
    },
    "aqua": {
        "hex": "#00ffff",
        "rgb": [
            0,
            255,
            255
        ]
    },
    "aquamarine": {
        "hex": "#7fffd4",
        "rgb": [
            127,
            255,
            212
        ]
    },
    "azure": {
        "hex": "#f0ffff",
        "rgb": [
            240,
            255,
            255
        ]
    },
    "beige": {
        "hex": "#f5f5dc",
        "rgb": [
            245,
            245,
            220
        ]
    },
    "bisque": {
        "hex": "#ffe4c4",
        "rgb": [
            255,
            228,
            196
        ]
    },
    "black": {
        "hex": "#000000",
        "rgb": [
            0,
            0,
            0
        ]
    },
    "blanchedalmond": {
        "hex": "#ffebcd",
        "rgb": [
            255,
            235,
            205
        ]
    },
    "blue": {
        "hex": "#0000ff",
        "rgb": [
            0,
            0,
            255
        ]
    },
    "blueviolet": {
        "hex": "#8a2be2",
        "rgb": [
            138,
            43,
            226
        ]
    },
    "brown": {
        "hex": "#a52a2a",
        "rgb": [
            165,
            42,
            42
        ]
    },
    "burlywood": {
        "hex": "#deb887",
        "rgb": [
            222,
            184,
            135
        ]
    },
    "cadetblue": {
        "hex": "#5f9ea0",
        "rgb": [
            95,
            158,
            160
        ]
    },
    "chartreuse": {
        "hex": "#7fff00",
        "rgb": [
            127,
            255,
            0
        ]
    },
    "chocolate": {
        "hex": "#d2691e",
        "rgb": [
            210,
            105,
            30
        ]
    },
    "coral": {
        "hex": "#ff7f50",
        "rgb": [
            255,
            127,
            80
        ]
    },
    "cornflowerblue": {
        "hex": "#6495ed",
        "rgb": [
            100,
            149,
            237
        ]
    },
    "cornsilk": {
        "hex": "#fff8dc",
        "rgb": [
            255,
            248,
            220
        ]
    },
    "crimson": {
        "hex": "#dc143c",
        "rgb": [
            220,
            20,
            60
        ]
    },
    "cyan": {
        "hex": "#00ffff",
        "rgb": [
            0,
            255,
            255
        ]
    },
    "darkblue": {
        "hex": "#00008b",
        "rgb": [
            0,
            0,
            139
        ]
    },
    "darkcyan": {
        "hex": "#008b8b",
        "rgb": [
            0,
            139,
            139
        ]
    },
    "darkgoldenrod": {
        "hex": "#b8860b",
        "rgb": [
            184,
            134,
            11
        ]
    },
    "darkgray": {
        "hex": "#a9a9a9",
        "rgb": [
            169,
            169,
            169
        ]
    },
    "darkgreen": {
        "hex": "#006400",
        "rgb": [
            0,
            100,
            0
        ]
    },
    "darkgrey": {
        "hex": "#a9a9a9",
        "rgb": [
            169,
            169,
            169
        ]
    },
    "darkkhaki": {
        "hex": "#bdb76b",
        "rgb": [
            189,
            183,
            107
        ]
    },
    "darkmagenta": {
        "hex": "#8b008b",
        "rgb": [
            139,
            0,
            139
        ]
    },
    "darkolivegreen": {
        "hex": "#556b2f",
        "rgb": [
            85,
            107,
            47
        ]
    },
    "darkorange": {
        "hex": "#ff8c00",
        "rgb": [
            255,
            140,
            0
        ]
    },
    "darkorchid": {
        "hex": "#9932cc",
        "rgb": [
            153,
            50,
            204
        ]
    },
    "darkred": {
        "hex": "#8b0000",
        "rgb": [
            139,
            0,
            0
        ]
    },
    "darksalmon": {
        "hex": "#e9967a",
        "rgb": [
            233,
            150,
            122
        ]
    },
    "darkseagreen": {
        "hex": "#8fbc8f",
        "rgb": [
            143,
            188,
            143
        ]
    },
    "darkslateblue": {
        "hex": "#483d8b",
        "rgb": [
            72,
            61,
            139
        ]
    },
    "darkslategray": {
        "hex": "#2f4f4f",
        "rgb": [
            47,
            79,
            79
        ]
    },
    "darkslategrey": {
        "hex": "#2f4f4f",
        "rgb": [
            47,
            79,
            79
        ]
    },
    "darkturquoise": {
        "hex": "#00ced1",
        "rgb": [
            0,
            206,
            209
        ]
    },
    "darkviolet": {
        "hex": "#9400d3",
        "rgb": [
            148,
            0,
            211
        ]
    },
    "deeppink": {
        "hex": "#ff1493",
        "rgb": [
            255,
            20,
            147
        ]
    },
    "deepskyblue": {
        "hex": "#00bfff",
        "rgb": [
            0,
            191,
            255
        ]
    },
    "dimgray": {
        "hex": "#696969",
        "rgb": [
            105,
            105,
            105
        ]
    },
    "dimgrey": {
        "hex": "#696969",
        "rgb": [
            105,
            105,
            105
        ]
    },
    "dodgerblue": {
        "hex": "#1e90ff",
        "rgb": [
            30,
            144,
            255
        ]
    },
    "firebrick": {
        "hex": "#b22222",
        "rgb": [
            178,
            34,
            34
        ]
    },
    "floralwhite": {
        "hex": "#fffaf0",
        "rgb": [
            255,
            250,
            240
        ]
    },
    "forestgreen": {
        "hex": "#228b22",
        "rgb": [
            34,
            139,
            34
        ]
    },
    "fuchsia": {
        "hex": "#ff00ff",
        "rgb": [
            255,
            0,
            255
        ]
    },
    "gainsboro": {
        "hex": "#dcdcdc",
        "rgb": [
            220,
            220,
            220
        ]
    },
    "ghostwhite": {
        "hex": "#f8f8ff",
        "rgb": [
            248,
            248,
            255
        ]
    },
    "goldenrod": {
        "hex": "#daa520",
        "rgb": [
            218,
            165,
            32
        ]
    },
    "gold": {
        "hex": "#ffd700",
        "rgb": [
            255,
            215,
            0
        ]
    },
    "gray": {
        "hex": "#808080",
        "rgb": [
            128,
            128,
            128
        ]
    },
    "green": {
        "hex": "#008000",
        "rgb": [
            0,
            128,
            0
        ]
    },
    "greenyellow": {
        "hex": "#adff2f",
        "rgb": [
            173,
            255,
            47
        ]
    },
    "grey": {
        "hex": "#808080",
        "rgb": [
            128,
            128,
            128
        ]
    },
    "honeydew": {
        "hex": "#f0fff0",
        "rgb": [
            240,
            255,
            240
        ]
    },
    "hotpink": {
        "hex": "#ff69b4",
        "rgb": [
            255,
            105,
            180
        ]
    },
    "indianred": {
        "hex": "#cd5c5c",
        "rgb": [
            205,
            92,
            92
        ]
    },
    "indigo": {
        "hex": "#4b0082",
        "rgb": [
            75,
            0,
            130
        ]
    },
    "ivory": {
        "hex": "#fffff0",
        "rgb": [
            255,
            255,
            240
        ]
    },
    "khaki": {
        "hex": "#f0e68c",
        "rgb": [
            240,
            230,
            140
        ]
    },
    "lavenderblush": {
        "hex": "#fff0f5",
        "rgb": [
            255,
            240,
            245
        ]
    },
    "lavender": {
        "hex": "#e6e6fa",
        "rgb": [
            230,
            230,
            250
        ]
    },
    "lawngreen": {
        "hex": "#7cfc00",
        "rgb": [
            124,
            252,
            0
        ]
    },
    "lemonchiffon": {
        "hex": "#fffacd",
        "rgb": [
            255,
            250,
            205
        ]
    },
    "lightblue": {
        "hex": "#add8e6",
        "rgb": [
            173,
            216,
            230
        ]
    },
    "lightcoral": {
        "hex": "#f08080",
        "rgb": [
            240,
            128,
            128
        ]
    },
    "lightcyan": {
        "hex": "#e0ffff",
        "rgb": [
            224,
            255,
            255
        ]
    },
    "lightgoldenrodyellow": {
        "hex": "#fafad2",
        "rgb": [
            250,
            250,
            210
        ]
    },
    "lightgray": {
        "hex": "#d3d3d3",
        "rgb": [
            211,
            211,
            211
        ]
    },
    "lightgreen": {
        "hex": "#90ee90",
        "rgb": [
            144,
            238,
            144
        ]
    },
    "lightgrey": {
        "hex": "#d3d3d3",
        "rgb": [
            211,
            211,
            211
        ]
    },
    "lightpink": {
        "hex": "#ffb6c1",
        "rgb": [
            255,
            182,
            193
        ]
    },
    "lightsalmon": {
        "hex": "#ffa07a",
        "rgb": [
            255,
            160,
            122
        ]
    },
    "lightseagreen": {
        "hex": "#20b2aa",
        "rgb": [
            32,
            178,
            170
        ]
    },
    "lightskyblue": {
        "hex": "#87cefa",
        "rgb": [
            135,
            206,
            250
        ]
    },
    "lightslategray": {
        "hex": "#778899",
        "rgb": [
            119,
            136,
            153
        ]
    },
    "lightslategrey": {
        "hex": "#778899",
        "rgb": [
            119,
            136,
            153
        ]
    },
    "lightsteelblue": {
        "hex": "#b0c4de",
        "rgb": [
            176,
            196,
            222
        ]
    },
    "lightyellow": {
        "hex": "#ffffe0",
        "rgb": [
            255,
            255,
            224
        ]
    },
    "lime": {
        "hex": "#00ff00",
        "rgb": [
            0,
            255,
            0
        ]
    },
    "limegreen": {
        "hex": "#32cd32",
        "rgb": [
            50,
            205,
            50
        ]
    },
    "linen": {
        "hex": "#faf0e6",
        "rgb": [
            250,
            240,
            230
        ]
    },
    "magenta": {
        "hex": "#ff00ff",
        "rgb": [
            255,
            0,
            255
        ]
    },
    "maroon": {
        "hex": "#800000",
        "rgb": [
            128,
            0,
            0
        ]
    },
    "mediumaquamarine": {
        "hex": "#66cdaa",
        "rgb": [
            102,
            205,
            170
        ]
    },
    "mediumblue": {
        "hex": "#0000cd",
        "rgb": [
            0,
            0,
            205
        ]
    },
    "mediumorchid": {
        "hex": "#ba55d3",
        "rgb": [
            186,
            85,
            211
        ]
    },
    "mediumpurple": {
        "hex": "#9370db",
        "rgb": [
            147,
            112,
            219
        ]
    },
    "mediumseagreen": {
        "hex": "#3cb371",
        "rgb": [
            60,
            179,
            113
        ]
    },
    "mediumslateblue": {
        "hex": "#7b68ee",
        "rgb": [
            123,
            104,
            238
        ]
    },
    "mediumspringgreen": {
        "hex": "#00fa9a",
        "rgb": [
            0,
            250,
            154
        ]
    },
    "mediumturquoise": {
        "hex": "#48d1cc",
        "rgb": [
            72,
            209,
            204
        ]
    },
    "mediumvioletred": {
        "hex": "#c71585",
        "rgb": [
            199,
            21,
            133
        ]
    },
    "midnightblue": {
        "hex": "#191970",
        "rgb": [
            25,
            25,
            112
        ]
    },
    "mintcream": {
        "hex": "#f5fffa",
        "rgb": [
            245,
            255,
            250
        ]
    },
    "mistyrose": {
        "hex": "#ffe4e1",
        "rgb": [
            255,
            228,
            225
        ]
    },
    "moccasin": {
        "hex": "#ffe4b5",
        "rgb": [
            255,
            228,
            181
        ]
    },
    "navajowhite": {
        "hex": "#ffdead",
        "rgb": [
            255,
            222,
            173
        ]
    },
    "navy": {
        "hex": "#000080",
        "rgb": [
            0,
            0,
            128
        ]
    },
    "oldlace": {
        "hex": "#fdf5e6",
        "rgb": [
            253,
            245,
            230
        ]
    },
    "olive": {
        "hex": "#808000",
        "rgb": [
            128,
            128,
            0
        ]
    },
    "olivedrab": {
        "hex": "#6b8e23",
        "rgb": [
            107,
            142,
            35
        ]
    },
    "orange": {
        "hex": "#ffa500",
        "rgb": [
            255,
            165,
            0
        ]
    },
    "orangered": {
        "hex": "#ff4500",
        "rgb": [
            255,
            69,
            0
        ]
    },
    "orchid": {
        "hex": "#da70d6",
        "rgb": [
            218,
            112,
            214
        ]
    },
    "palegoldenrod": {
        "hex": "#eee8aa",
        "rgb": [
            238,
            232,
            170
        ]
    },
    "palegreen": {
        "hex": "#98fb98",
        "rgb": [
            152,
            251,
            152
        ]
    },
    "paleturquoise": {
        "hex": "#afeeee",
        "rgb": [
            175,
            238,
            238
        ]
    },
    "palevioletred": {
        "hex": "#db7093",
        "rgb": [
            219,
            112,
            147
        ]
    },
    "papayawhip": {
        "hex": "#ffefd5",
        "rgb": [
            255,
            239,
            213
        ]
    },
    "peachpuff": {
        "hex": "#ffdab9",
        "rgb": [
            255,
            218,
            185
        ]
    },
    "peru": {
        "hex": "#cd853f",
        "rgb": [
            205,
            133,
            63
        ]
    },
    "pink": {
        "hex": "#ffc0cb",
        "rgb": [
            255,
            192,
            203
        ]
    },
    "plum": {
        "hex": "#dda0dd",
        "rgb": [
            221,
            160,
            221
        ]
    },
    "powderblue": {
        "hex": "#b0e0e6",
        "rgb": [
            176,
            224,
            230
        ]
    },
    "purple": {
        "hex": "#800080",
        "rgb": [
            128,
            0,
            128
        ]
    },
    "rebeccapurple": {
        "hex": "#663399",
        "rgb": [
            102,
            51,
            153
        ]
    },
    "red": {
        "hex": "#ff0000",
        "rgb": [
            255,
            0,
            0
        ]
    },
    "rosybrown": {
        "hex": "#bc8f8f",
        "rgb": [
            188,
            143,
            143
        ]
    },
    "royalblue": {
        "hex": "#4169e1",
        "rgb": [
            65,
            105,
            225
        ]
    },
    "saddlebrown": {
        "hex": "#8b4513",
        "rgb": [
            139,
            69,
            19
        ]
    },
    "salmon": {
        "hex": "#fa8072",
        "rgb": [
            250,
            128,
            114
        ]
    },
    "sandybrown": {
        "hex": "#f4a460",
        "rgb": [
            244,
            164,
            96
        ]
    },
    "seagreen": {
        "hex": "#2e8b57",
        "rgb": [
            46,
            139,
            87
        ]
    },
    "seashell": {
        "hex": "#fff5ee",
        "rgb": [
            255,
            245,
            238
        ]
    },
    "sienna": {
        "hex": "#a0522d",
        "rgb": [
            160,
            82,
            45
        ]
    },
    "silver": {
        "hex": "#c0c0c0",
        "rgb": [
            192,
            192,
            192
        ]
    },
    "skyblue": {
        "hex": "#87ceeb",
        "rgb": [
            135,
            206,
            235
        ]
    },
    "slateblue": {
        "hex": "#6a5acd",
        "rgb": [
            106,
            90,
            205
        ]
    },
    "slategray": {
        "hex": "#708090",
        "rgb": [
            112,
            128,
            144
        ]
    },
    "slategrey": {
        "hex": "#708090",
        "rgb": [
            112,
            128,
            144
        ]
    },
    "snow": {
        "hex": "#fffafa",
        "rgb": [
            255,
            250,
            250
        ]
    },
    "springgreen": {
        "hex": "#00ff7f",
        "rgb": [
            0,
            255,
            127
        ]
    },
    "steelblue": {
        "hex": "#4682b4",
        "rgb": [
            70,
            130,
            180
        ]
    },
    "tan": {
        "hex": "#d2b48c",
        "rgb": [
            210,
            180,
            140
        ]
    },
    "teal": {
        "hex": "#008080",
        "rgb": [
            0,
            128,
            128
        ]
    },
    "thistle": {
        "hex": "#d8bfd8",
        "rgb": [
            216,
            191,
            216
        ]
    },
    "tomato": {
        "hex": "#ff6347",
        "rgb": [
            255,
            99,
            71
        ]
    },
    "turquoise": {
        "hex": "#40e0d0",
        "rgb": [
            64,
            224,
            208
        ]
    },
    "violet": {
        "hex": "#ee82ee",
        "rgb": [
            238,
            130,
            238
        ]
    },
    "wheat": {
        "hex": "#f5deb3",
        "rgb": [
            245,
            222,
            179
        ]
    },
    "white": {
        "hex": "#ffffff",
        "rgb": [
            255,
            255,
            255
        ]
    },
    "whitesmoke": {
        "hex": "#f5f5f5",
        "rgb": [
            245,
            245,
            245
        ]
    },
    "yellow": {
        "hex": "#ffff00",
        "rgb": [
            255,
            255,
            0
        ]
    },
    "yellowgreen": {
        "hex": "#9acd32",
        "rgb": [
            154,
            205,
            50
        ]
    }
}