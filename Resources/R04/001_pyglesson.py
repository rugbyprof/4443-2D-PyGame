"""
Pygame 001

Description:

    Creating a simple window with pygame.

Methods:
    - pygame.init: Starts everything off
    - pygame.display.set_mode: Creates the window
    - pygame.display.set_caption: Adds text to actual window (not game screen)

"""
# Import and initialize the pygame library
import pygame

def main():
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Basic Empty Window')

    # Set up the drawing window
    pygame.display.set_mode([500, 500])

    # Run until the user asks to quit
    # game loop
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    main()