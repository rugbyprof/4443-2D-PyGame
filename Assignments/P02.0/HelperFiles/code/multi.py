import pygame
import pygame.freetype
import random
import os
import sys
import json
import pprint
import glob
import more_itertools 

from helper_functions import loadSpriteImages
from helper_functions import loadJson
from helper_classes import Colors

# Our typical config, but a lot smaller right now.
config = {
    'title' :'P02.001 ',
    'window_size' : (1000,500),
    'sprite_sheets':{
        'mario':{'path':'../resources/mario_frames'}
    },
    'tiles_path':'../resources/maps/forest_tileset/Tiles_20',
    'levels_path':"../resources/levels",
    'tile_size':20,
    'debug': True,
    'debug_level':20
    }


def debug(statement,level=0):
    """ An easy way to globally turn on and off debug statements. Just change config['debug'] to False
    """
    if config['debug']:
        if level <= config['debug_level']:
            print(statement)

#https://gist.github.com/programmingpixels/27b7f8f59ec53b401183c68f4be1634b#file-step4-py

# def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
#     """ Returns surface with text written on """
#     font = pygame.freetype.SysFont("Courier", font_size, bold=True)
#     surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
#     return surface.convert_alpha()

# class UIElement(pygame.sprite.Sprite):
#     """ An user interface element that can be added to a surface """

#     def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
#         """
#         Args:
#             center_position - tuple (x, y)
#             text - string of text to write
#             font_size - int
#             bg_rgb (background colour) - tuple (r, g, b)
#             text_rgb (text colour) - tuple (r, g, b)
#             action - the gamestate change associated with this button
#         """
#         self.mouse_over = False

#         default_image = create_surface_with_text(
#             text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
#         )

#         highlighted_image = create_surface_with_text(
#             text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
#         )

#         self.images = [default_image, highlighted_image]

#         self.rects = [
#             default_image.get_rect(center=center_position),
#             highlighted_image.get_rect(center=center_position),
#         ]

#         self.action = action

#         super().__init__()

#     @property
#     def image(self):
#         return self.images[1] if self.mouse_over else self.images[0]

#     @property
#     def rect(self):
#         return self.rects[1] if self.mouse_over else self.rects[0]

#     def update(self, mouse_pos, mouse_up):
#         """ Updates the mouse_over variable and returns the button's
#             action value when clicked.
#         """
#         if self.rect.collidepoint(mouse_pos):
#             self.mouse_over = True
#             if mouse_up:
#                 return self.action
#         else:
#             self.mouse_over = False

#     def draw(self, surface):
#         """ Draws element onto a surface """
#         surface.blit(self.image, self.rect)

class State(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


class GameMenu(State):

    def __init__(self):
        super(State, self).__init__()

        self.bg_color = Colors.RGB('mediumorchid')
        self.fg_color = Colors.RGB('white')
        self.game_width,self.game_height = config['window_size']

        self.fonts = {}

        self.fonts[56] = pygame.font.SysFont('Arial', 56)
        self.fonts[32] = pygame.font.SysFont('Arial', 32)

        self.menuChoices = []

        mid_x = config['window_size'][0]//2
        mid_y = config['window_size'][1]//2

        self.addChoice(text="Crazy Game",loc=(mid_x,mid_y),font_size=56,font_color=Colors.RGB('white'))
        self.addChoice(text="> press space to start <",loc=(mid_x,mid_y+50),font_size=32,font_color=Colors.RGB('white'))
        

    def addChoice(self,**kwargs):

        text = kwargs.get('text',None)
        loc = kwargs.get('loc',(0,0))
        font_size = kwargs.get('font_size',56)
        font_color = kwargs.get('font_color',Colors.RGB("black"))

        if not font_size in self.fonts:
            self.fonts[font_size] = pygame.font.SysFont('Arial', font_size)

        text_width, text_height = self.fonts[font_size].size(text)

        loc = (loc[0]-text_width//2,loc[1])

        choice = {
            'text':text,
            'loc':loc,
            'font_size':font_size,
            'font_color':font_color
        }

        self.menuChoices.append(choice)


    def render(self,screen):
        screen.fill(self.bg_color)
        for item in self.menuChoices:
            
            temp = self.fonts[item['font_size']].render(item['text'], True, item['font_color'])
            
            screen.blit(temp, item['loc'])

    def update(self):
        pass

    def handle_events(self,events):
        print(events)
        for e in events:
            print(e.type)
            if e.type == pygame.MOUSEBUTTONUP:
                print("here I am johnny!")
                self.manager.go_to()


class LevelLoader(State):

    def __init__(self,**kwargs):
        super(State, self).__init__()

        self.tiles_path = kwargs.get('tiles_path',None)
        if self.tiles_path == None:
            print(f"Error: No path to the tile set!!")
            sys.exit()

        if not os.path.isdir(self.tiles_path):
            print(f"Error: {self.tiles_path} is not a directory!")
            sys.exit()

        self.levels_path= kwargs.get('levels_path',None)
        self.level_name = kwargs.get('level_name',None)
        self.tile_size = kwargs.get('tile_size',None)

        if self.tile_size != None:
            if type(self.tile_size) == int:
                self.tile_size = (self.tile_size,self.tile_size)

        self.tiles = []
        self.tile_sprites = []

        self.tiles_group = pygame.sprite.Group()

        if self.tiles_path != None:
            self.loadTiles()

        if self.level_name != None:
            self.loadLevel()

        
    def loadTiles(self):
        self.tiles = glob.glob(os.path.join(self.tiles_path,"*.png"))
        self.tiles.sort()


    def loadLevel(self,level_name=None,levels_path=None):
        if levels_path is None and self.levels_path is None:
            print(f"Error: Need a directory to read levels from!")
            sys.exit()

        if levels_path != None:
            self.levels_path = levels_path

        with open(os.path.join(self.levels_path,self.level_name),"r") as f:
            data = f.readlines()

        row = 0         # which row on the screen
        col = 0         # which col on the screen
        for line in data:
            line = line.strip()
            for code in more_itertools.chunked(line, 2):
                tilenum = code[0]+code[1]
                if tilenum != "..":
                    tile_loc = os.path.join(self.tiles_path,tilenum+".png")
                    print(tile_loc)
                    if os.path.isfile(tile_loc):
                        img = pygame.image.load(tile_loc)
                        tile = pygame.sprite.Sprite()
                        tile.image = pygame.transform.scale(img, (self.tile_size[0], self.tile_size[0]))
                        tile.rect = tile.image.get_rect()
                        print(row,col)
                        tile.rect.x = col * self.tile_size[0]   # set pygame screen position
                        tile.rect.y = row * self.tile_size[1]
                        self.tile_sprites.append(tile)
                        self.tiles_group.add(tile)
                col += 1
            col = 0
            row += 1

    def render(self, screen):
        self.tiles_group.update()
        self.tiles_group.draw(screen)

    def update(self):
        pass

    def handle_events(self,events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONUP:
                self.manager.go_to()


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class StateMananger(Borg):
    def __init__(self):
        self.index = -1
        self.states = [
            GameMenu(),
            LevelLoader(levels_path=config['levels_path'],tiles_path=config['tiles_path'],level_name="level_01",tile_size=(20,20)),
            LevelLoader(levels_path=config['levels_path'],tiles_path=config['tiles_path'],level_name="level_02",tile_size=(20,20)),
            LevelLoader(levels_path=config['levels_path'],tiles_path=config['tiles_path'],level_name="level_03",tile_size=(20,20))
        ]
        self.go_to()

    def go_to(self):
        self.index = (self.index + 1) % len(self.states)
        print(self.index)
        self.state = self.states[self.index]
        self.state.manager = self
        


###############################################################################
#   _ __ ___   __ _(_)_ __  
#  | '_ ` _ \ / _` | | '_ \ 
#  | | | | | | (_| | | | | |
#  |_| |_| |_|\__,_|_|_| |_|
###############################################################################          
def main():
    pygame.init()

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    manager = StateMananger()

    # Run until the user asks to quit
    # Basic game loop
    running = True
    while running:

        screen.fill((0,0,0))


        events = pygame.event.get()
        # Did the user click the window close button?
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            # Not used in this instance of our game
            if event.type == pygame.MOUSEBUTTONUP:
                # debug(pygame.mouse.get_pos(),10)
                pass

        manager.state.handle_events(events)
        manager.state.update()
        manager.state.render(screen)

        pygame.display.flip()

    pygame.quit()

if __name__=='__main__':

    main()

