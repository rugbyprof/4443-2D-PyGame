"""
Pygame 005

Description:

   Simple config starter
   And drawing a ball

New Code:

    - pygame.draw.circle(screen, (red, green, blue), (250, 250), 75)

"""

config = {
    'title' :'005 Pygame Lesson'
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
    screen = pygame.display.set_mode([500, 500])


    # Run until the user asks to quit
    # game loop
    running = True
    while running:

        screen.fill(colors['background'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        red = int(random.random() * 255)
        green = int(random.random() * 255)
        blue = int(random.random() * 255)

        pygame.draw.circle(screen, (red, green, blue), (250, 250), 75)


        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    main()