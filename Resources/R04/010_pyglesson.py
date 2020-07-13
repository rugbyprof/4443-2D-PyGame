"""
Pygame 010

Description:

   Fixing our Ball Class Part 1

New Code:

    None

"""
# Import and initialize the pygame library
import pygame
import random
import json
import pprint
import sys

def load_colors(infile):
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
        dx <int>                : x direction
        dy <int                 : y direction
        speed <int>             : number of pixels to jump every update
    Methods;
        __init__(pygame.display,rgb tuple,int ,int ,int)
        Draw(None)
        Move(int,int)
    """
    def __init__(self,screen,color,x,y,r):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = r
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        self.speed = 15

    def Draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def Move(self):
        """Move: Updates the location of the ball based on:
                    direction
                    current location
                    speed
                Also reverses direction when a "collision" occurs.
                Collision = x,y coord of circle leaves bounds of window.
                            we will tighten that definition up later using
                            bounding rectangles.
        """
        w, h = pygame.display.get_surface().get_size()

        self.x += (self.speed * self.dx)
        self.y += (self.speed * self.dy)

        if self.x <= 0 or self.x >= w:
            self.dx *= -1

        if self.y <= 0 or self.y >= h:
            self.dy *= -1


def main():
    pygame.init()

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    # set circle location
    x = 20
    y = 250

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
        b1.Move()


        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    #colors = fix_colors("colors.json")
    #pprint.pprint(colors)
    main()
