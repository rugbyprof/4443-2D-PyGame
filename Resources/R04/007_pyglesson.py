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
    new_colors = {}
    with open(infile,'r') as f:
        data = f.read()
        colors = json.loads(data)

        for name,hex in colors.items():
            new_colors[name] = {}
            new_colors[name]['hex'] = hex
            red = int(hex[1:3],16)
            green = int(hex[3:5],16)
            blue = int(hex[5:],16)
            rgb = (red,green,blue)
            new_colors[name]['rgb'] = rgb
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
