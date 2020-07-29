import helper_module
from helper_module import *

class Bullet(SimpleAnimation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Player(PlayerAnimation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self):
        """ Updating players state
        """
        
        self.move() # update dx and dy

        old_action = self.action

        # use dx and dy to pick action (direction)
        self.action  = self.choose_animation()

        # if for some reason no action is chosen
        # use the "old action" to choose image with
        if self.action == '':
            self.action = old_action
            center = self.rect.center
            self.image = self.sprites[old_action][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            return

        # if we found an "action" then use it to set image
        self.image = self.sprites[self.action][self.frame]


        now = pygame.time.get_ticks()                           # get current game clock
        if now - self.last_update > self.frame_rate:            # has enough time passed to move?   
            self.last_update = now                              # if so reset the clock
            self.frame += 1                                     # get next animation frame
            if self.frame == len(self.sprites[self.action]):    # if at end goto begin ( assembly :) lol)
                self.frame = 0
            else:   
                center = self.rect.center                       # display next frame in animation
                self.image = self.sprites[self.action][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def main():
    pygame.init()
    pressed = None          # which key pressed
    running = True          # game loop runs till told to quit
    mouse_location = None   # holds mouse location if event is fired

    # sets the window title
    pygame.display.set_caption(config['title'])

    # Game size of game window from config
    width = config['window_size']['width']
    height = config['window_size']['height']

    # Set up the drawing window
    screen = pygame.display.set_mode((width,height))

    # load our background
    background = pygame.image.load(config['background'])

    # sprite group to handle all the visuals
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    # help control event timing
    clock = pygame.time.Clock()

    player = Player(path=config['sprite_sheets']['pac_man_orange']['path'],loc=(random.randint(0,width),random.randint(0,height)),speed=10,dx=1,dy=1)

    player_group.add(player)

    all_sprites.add(player)

    # game loop
    while running:

        clock.tick(config['fps'])

        # fill screen with white
        screen.fill(colorsDict['lightgray']['rgb'])

        # show background grid (no moving it)
        screen.blit(background, (0,0),(0,0,width,height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                pressed = event.key

            if event.type == pygame.KEYUP:
                pressed = event.key

            if event.type == pygame.MOUSEMOTION:
                mouse_location = pygame.mouse.get_pos()
                
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_location = pygame.mouse.get_pos()

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':

    main()