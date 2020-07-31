class FloorLoader(pygame.sprite.Sprite):
    """ 
    """
    def __init__(self, **kwargs):

        # Initialize parent
        pygame.sprite.Sprite.__init__(self)

        self.floor_path = kwargs.get('floor_path',None)
        if not self.floor_path:
            print("Error: Need path to map of floor!")
            sys.exit(0)

        self.tile_size = kwargs.get('tile_size',10)

        f = open(self.floor_path,"r")
        self.map_file = f.readlines()

        # make empty floor
        self.floor = [[] for x in range(config['window_size'][1])]

        for i in range(config['window_size'][0]):
            self.floor[i] = [0 for x in range(config['window_size'][0])]

        i = 0
        for row in self.map_file:
            j = 0
            for col in row:
                if col == 'x':
                    self.floor[i][j] = pygame.image.load('blank_tile.png')
                j += 1
            i += 

    def readFile(self):


    def loadFloor(self):
        img = pygame.image.load('stone.png')

        block = pygame.sprite.Sprite()
        block.image = pygame.transform.scale(img, (64, 64))

