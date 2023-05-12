import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        self.pos = None
        self.type = None
        self.image = None
        self.color = None
        self.rect = None

        self.size = None
        self.speed = pygame.Vector2(10, 10)
        self.distance_to_target = pygame.Vector2()

        self.active = False

    def motion(self, target: (int, int), dt):
        target = pygame.Vector2(target)
        current_pos = pygame.Vector2(self.rect.centerx, self.rect.centery)
        self.distance_to_target = (target - current_pos)

        current_pos.x += self.distance_to_target.x * self.speed.x * dt
        current_pos.y += self.distance_to_target.y * self.speed.y * dt

        self.rect.centerx = current_pos.x
        self.rect.centery = current_pos.y

    def scale(self, value, dt):
        target = value - 1
        distance_to_target = target - self.size
        self.size += distance_to_target * self.speed.x * 2 * dt

    def custom_draw(self):
        new_image = pygame.transform.smoothscale(self.image, (self.size, self.size))
        self.rect.width = self.size
        self.rect.height = self.size
        screen = pygame.display.get_surface()
        screen.blit(new_image, self.rect)

    def update(self):
        pass


class King(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.type = "King"
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_klt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_kdt45.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))
        self.size = self.rect.width


class Queen(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.type = "Queen"
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_qlt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_qdt45.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))
        self.size = self.rect.width


class Rook(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.type = "Rook"
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_rlt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_rdt45.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))
        self.size = self.rect.width


class Bishop(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.type = "Bishop"
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_blt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_bdt45.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))
        self.size = self.rect.width

class Knight(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.type = "Knight"
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_nlt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_ndt45.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))
        self.size = self.rect.width

class Pawn(Piece):

    def __init__(self, pos, color, group):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.type = "Pawn"
        if color == 'light':
            self.image = pygame.image.load('images/pieces/Chess_plt45.png')
        elif color == 'dark':
            self.image = pygame.image.load('images/pieces/Chess_pdt45.png')
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(pos.x * self.image.get_width(), pos.y * self.image.get_height()))
        self.size = self.rect.width




