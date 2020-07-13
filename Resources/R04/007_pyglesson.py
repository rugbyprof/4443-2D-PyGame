"""
Pygame 007

Description:

   Add a colors file

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
        infile <string> : path to an input json file to be processed.
                          expects a format like:
                            {
                                "color_name" : "#hexvalue",
                                ...
                            }
    Notes:
        There are more concise ways to convert the hex values (list comprehensions for one).
        I went for a readable approach (for me and you ...)
    """
    # new dictionary to store rgb values as well
    new_colors = {}

    # "with" is one way to open a file where
    # the file is "closed" after the code block
    # is completed. Nice and efficient and clean
    with open(infile,'r') as f:
        data = f.read()             # read all data in at once (1 big string)
        colors = json.loads(data)   # use the json library to convert string to
                                    # dictionary. Warning: no checks for valid
                                    # json were done, or valid paths

        # loop throug dictionary (duh)
        for name,hex in colors.items():
            new_colors[name] = {}           # puts a new dictionary at that color name
                                            # e.g. new_colors = {
                                            #   "red" = {}
                                            # }


            new_colors[name]['hex'] = hex   # e.g. new_colors = {
                                            #   "red" : {
                                            #      "hex": "#FF0000"
                                            #   }
                                            # }


            red = int(hex[1:3],16)
            green = int(hex[3:5],16)
            blue = int(hex[5:],16)
            rgb = (red,green,blue)
            new_colors[name]['rgb'] = rgb   # e.g. new_colors = {
                                            #   "red" : {
                                            #      "hex": "#FF0000",
                                            #      "rgb": (255,0,0)
                                            #   }
                                            # }

    return new_colors




config = {
    'title' :'006 Pygame Lesson',
    'window_size' : (500,500)
}

colors = {}


def main():
    pygame.init()

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    # set circle location
    x = 50
    y = 50

    # Run until the user asks to quit
    # game loop
    running = True
    while running:

        screen.fill(colors['peachpuff']['rgb'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.draw.circle(screen, colors['mediumturquoise']['rgb'], (x, y), 50)

        x += 10
        y += 10

        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':

    colors = load_colors("colors.json")
    pprint.pprint(colors)
    main()
