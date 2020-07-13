"""
Pygame 006

Description:

   Moving the ball ... poorly

New Code:

    None

"""

config = {
    'title' :'006 Pygame Lesson',
    'window_size' : (500,500)
}

colors = {
    'magenta':(255, 0, 255, 100),
    'cyan':(0, 255, 255, 100),
    'background':(0,130,200,100),
    'pink': (212,7,234,100)
}

# Import and initialize the pygame library
import pygame
import random

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

        screen.fill(colors['background'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.draw.circle(screen, colors['pink'], (x, y), 50)

        x += 10
        y += 10


        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    main()