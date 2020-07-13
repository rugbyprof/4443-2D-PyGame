"""
Pygame 009

Description:

   Writing a ball function or ... class??
   Wich is appropriate.

New Code:

    None

"""
# Import and initialize the pygame library
import pygame
import random
import json
import pprint

def load_colors(infile):
    """load_colors
    Params:
        infile <string> : path to color json file
    Returns:
        colors <json>
    ToDo:
        Exception handling for bad json and bad file path.
    """
    with open(infile,'r') as f:
        data = f.read()
        colors = json.loads(data)
    return colors

config = {
    'title' :'006 Pygame Lesson',
    'window_size' : (500,500)
}

colors = load_colors('colors2.json')

class Ball:
    """Ball: Represents a pygame instance of a circle
    Data Members:
        screen <pygame.display> : where to print the circle
        color <tuple>           : rgb value with alpha channel e.g. (123,111,88,100)
        x <int>                 : One part of a 2D point
        y <int>                 : One part of a 2D point
        r <int>                 : Radius in pixels
    Methods;
        __init__(pygame.display,rgb tuple,int ,int ,int)
        Draw(None)
        Move(int,int)
    """
    def __init__(self,screen,color,x,y,r):
        """ __init__
        Params:
            See Data Members.
        """
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = r

    def Draw(self):
        """Draw: Place the pygame circle onto the screen given the params
                 defined as data members.
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def Move(self,x,y):
        """Move: Re-assign the local x,y values of the circle essentially "moving"
                 the circle (crappy crappy crappy way of doing it.)
        """
        self.x = x
        self.y = y

def main():
    pygame.init()

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    # set circle location
    x = 50
    y = 50


    # construct the ball
    b1 = Ball(screen,colors['rebeccapurple']['rgb'],x,y,30)

    # Run until the user asks to quit
    # game loop
    running = True
    while running:

        screen.fill(colors['white']['rgb'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        b1.Draw()

        # update x,y here ...

        x += 10
        y += 10

        # And then move the ball ↑ defined up there ... bad juju!
        b1.Move(x,y)

        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    #colors = fix_colors("colors.json")
    #pprint.pprint(colors)
    main()
