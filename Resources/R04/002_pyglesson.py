"""
Pygame 002

Description:

    Loads an image from a file and uses it as the icon for the window.
    In osx, it uses it as the icon on the Dock.

New Code:

    # sets the icon path
    icon_path = os.path.join(u'images', u'icon_32.png')

    # loads the icon
    icon = pygame.image.load(icon_path)

    # sets the window icon
    pygame.display.set_icon(icon)



"""
# Import and initialize the pygame library
import pygame
import os

def main():
    pygame.init()


    # sets the icon path
    icon_path = os.path.join(u'images', u'icon_32.png')

    # loads the icon
    icon = pygame.image.load(icon_path)

    # sets the window icon
    pygame.display.set_icon(icon)

    # sets the window title
    pygame.display.set_caption(u'Basic Empty Window')

    # Set up the drawing window
    pygame.display.set_mode([500, 500])

    # Run until the user asks to quit
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