"""
Pygame 008

Description:

   Writing out the new colors file
   Randomly picking ball and screen colors

New Code:

    None

"""
# Import and initialize the pygame library
import pygame
import random
import json
import pprint

def fix_colors(infile):
    """ One time fix of original json file with only names and hex values.
        See previous lesson for commented function
    """
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

    f = open("colors2.json","w")
    f.write(json.dumps(new_colors))
    f.close()

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

# Calling the load_colors function turns "colors"
# into a python dictionary just like the "config"
# variable above (different structure but same idea)
colors = load_colors('colors2.json')

def main():
    pygame.init()

    # Pull the "keys" (color names in this case) out of
    # the colors dictionary
    names = list(colors.keys())

    # print them nice and pretty
    pprint.pprint(names)

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    # initial circle location
    x = 50
    y = 50

    # random.choice pulls a random value from
    # a list. If the list had 100 different
    # color names, then each name would have a
    # 1 percent change of being chosen.

    # Unless your name is Austin, then you would
    # bitch about the effectiveness of he random
    # implementation and your program would crash
    # blaming php for its issues :) Long story.
    # disregard after the 1 percent sentence.
    bcolor = random.choice(names)
    fcolor = random.choice(names)

    # Run until the user asks to quit
    # Basic game loop
    running = True
    while running:

        screen.fill(colors[bcolor]['rgb'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.draw.circle(screen, colors[fcolor]['rgb'], (x, y), 50)

        x += 10
        y += 10

        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    #colors = fix_colors("colors.json")
    #pprint.pprint(colors)
    main()
