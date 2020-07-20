import pygame as pg
import sys

# colors
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((640, 640))
        self.clock = pg.time.Clock()
        pg.key.set_repeat()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 100,100)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(GREY)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.rect)
        pg.display.flip()

    def events(self):
        for self.event in pg.event.get():
            if self.event.type == pg.QUIT:
                self.quit()


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((32,32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = [x, y]

    def get_keys(self):
        if self.game.event.type == pg.KEYDOWN:
            if self.game.event.key == pg.K_LEFT:
                self.pos[0] -= 1
                print("This should only be printed once per key press")

            elif self.game.event.key == pg.K_RIGHT:
                self.game.player.pos[0] += 1
                print("This should only be printed once per key press")

    def update(self):
        self.get_keys()
        self.rect.centery = self.pos[1]
        self.rect.centerx = self.pos[0]


g = Game()
while True:
    g.new()
    g.run()