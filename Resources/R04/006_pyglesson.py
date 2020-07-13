"""
Pygame 006

Description:

   Moving the ball the wrong way ...

New Code:

    - None

"""

config = {
    'title' :'Pygame Lesson 006',
    'game_width': 500,
    'game_height': 500,
    'window_size':[500,500]
}

colors = {
    'magenta':(255, 0, 255, 100),
    'cyan':(0, 255, 255, 100),
    'background':(0,130,200,100)
}

# Import and initialize the pygame library
import pygame
import random

def main():
    pygame.init()

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode([config['game_width'], config['game_width']])

    x = 50
    y = 50

    # Run until the user asks to quit
    # game loop
    running = True
    while running:

        screen.fill(colors['background'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.draw.circle(screen,colors['cyan'], (x, y), 50)

        x += 10
        y += 10


        pygame.display.flip()



    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    main()