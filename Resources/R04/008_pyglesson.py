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
    with open(infile,'r') as f:
        data = f.read()
        colors = json.loads(data)
    return colors

config = {
    'title' :'006 Pygame Lesson',
    'window_size' : (500,500)
}

colors = load_colors('colors2.json')

def main():
    pygame.init()

    names = list(colors.keys())
    pprint.pprint(names)

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode(config['window_size'])

    # set circle location
    x = 50
    y = 50

    bcolor = random.choice(names)
    fcolor = random.choice(names)

    # Run until the user asks to quit
    # game loop
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
