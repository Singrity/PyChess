import pygame
from piece import *
from states import CheckingPaths


class Board:
    BLACK = (50, 50, 50)
    GREY = (128, 128, 128)
    WHITE = (255, 255, 255)

    CELL_SIZE = 64

    def __init__(self):
        self.states = [CheckingPaths()]
        self.current_state = None
        self.pieces_sprites = pygame.sprite.Group()
        self.grid = []
        self.screen = pygame.display.get_surface()

        self.clicked = False
        self.active_piece = None

        King(pygame.Vector2(4, 0), "light", self.pieces_sprites)
        King(pygame.Vector2(4, 7), "dark", self.pieces_sprites)
        Queen(pygame.Vector2(3, 0), "light", self.pieces_sprites)
        Queen(pygame.Vector2(3, 7), "dark", self.pieces_sprites)

        Rook(pygame.Vector2(0, 0), "light", self.pieces_sprites)
        Rook(pygame.Vector2(0, 7), "dark", self.pieces_sprites)
        Rook(pygame.Vector2(7, 0), "light", self.pieces_sprites)
        Rook(pygame.Vector2(7, 7), "dark", self.pieces_sprites)

        Bishop(pygame.Vector2(2, 0), "light", self.pieces_sprites)
        Bishop(pygame.Vector2(2, 7), "dark", self.pieces_sprites)
        Bishop(pygame.Vector2(5, 0), "light", self.pieces_sprites)
        Bishop(pygame.Vector2(5, 7), "dark", self.pieces_sprites)

        Knight(pygame.Vector2(1, 0), "light", self.pieces_sprites)
        Knight(pygame.Vector2(1, 7), "dark", self.pieces_sprites)
        Knight(pygame.Vector2(6, 0), "light", self.pieces_sprites)
        Knight(pygame.Vector2(6, 7), "dark", self.pieces_sprites)

        [Pawn(pygame.Vector2(i, 1), "light", self.pieces_sprites) for i in range(8)]
        [Pawn(pygame.Vector2(i, 6), "dark", self.pieces_sprites) for i in range(8)]

        for x in range(self.screen.get_width() // self.CELL_SIZE):
            for y in range(self.screen.get_height() // self.CELL_SIZE):
                if (x + y) % 2 == 0:
                    self.grid.append((pygame.Rect(x * self.CELL_SIZE, y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), self.WHITE))
                else:
                    self.grid.append((pygame.Rect(x * self.CELL_SIZE, y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), self.BLACK))

    def update(self, was_clicked):
        mouse_pos = pygame.mouse.get_pos()
        if not self.active_piece:
            for piece in self.pieces_sprites:
                if was_clicked and piece.rect.collidepoint(mouse_pos):
                    self.active_piece = piece
                    break
        elif was_clicked:
            self.active_piece.rect.center = mouse_pos
        else:
            self.active_piece = None
        self.pieces_sprites.update()

    def draw(self):
        for rect, color in self.grid:
            pygame.draw.rect(self.screen, color, [rect.x, rect.y, self.CELL_SIZE, self.CELL_SIZE])
        self.pieces_sprites.draw(self.screen)



