"""
Pygame 004

Description:

   Still messing with surfaces and display items.

New Code:

    - Nothing really

"""
# Import and initialize the pygame library
import pygame

def main():
    pygame.init()

    # r g b a = red, green, blue, alpha
    # 0 - 255 is the range of values for each channel
    color = (0,130,200,100)
    magenta = (255, 0, 255, 100)
    cyan = (0, 255, 255, 100)

    # sets the window title
    pygame.display.set_caption(u'Coloring Surfaces')

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    # Create a surface that is 240x240 with an alpha channel turned on
    magenta_surface = pygame.Surface((240,240)).convert_alpha()
    # Fill said surface with an rgb tuple defined from above
    magenta_surface.fill(magenta)

    # Same as magenta
    cyan_surface = pygame.Surface((240, 240)).convert_alpha()
    cyan_surface.fill(cyan)

    # Fill the entire screen with "color"
    screen.fill(color)

    # Run until the user asks to quit
    # game loop
    running = True
    while running:

        screen.fill(color)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Blit copies the bits from surface to the screen at location (x,y)
        screen.blit(magenta_surface,(20,20))
        screen.blit(magenta_surface,(100,100))

        # Refresh display
        pygame.display.flip()


    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    main()