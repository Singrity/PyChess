import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = None
        self.color = None
        self.rect = None

        self.speed = pygame.Vector2()
        self.direction = pygame.Vector2()

        self.active = False

    def update(self):
        pass
        # new_x = (self.rect.centerx // 64) * 64
        # new_y = (self.rect.centery // 64) * 64
        # self.rect.x, self.rect.y = new_x, new_y


class King(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_klt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_kdt45.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))


class Queen(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_qlt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_qdt45.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))


class Rook(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_rlt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_rdt45.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))


class Bishop(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_blt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_bdt45.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))


class Knight(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_nlt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_ndt45.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))


class Pawn(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_plt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_pdt45.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))





