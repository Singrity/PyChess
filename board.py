import pygame
from piece import *
from states import CheckingPaths
from consts import INITIAL_POSITIONS


class Board:
    BLACK = (50, 50, 50)
    GREY = (128, 128, 128)
    WHITE = (255, 255, 255)

    CELL_SIZE = 64

    def __init__(self):

        self.pieces_sprites = pygame.sprite.Group()
        self.grid = {}
        self.screen = pygame.display.get_surface()

        self.initial_cell = None

        self.clicked = False
        self.active_piece = None

        self.build_board()

    def build_board(self):
        for x in range(self.screen.get_width() // self.CELL_SIZE):
            for y in range(self.screen.get_height() // self.CELL_SIZE):
                if (x + y) % 2 == 0:
                    self.grid[(x, y)] = {
                        "piece": None,
                        "color": self.WHITE
                    }
                else:
                    self.grid[(x, y)] = {
                        "piece": None,
                        "color": self.BLACK
                    }

        light_pieces = INITIAL_POSITIONS["light_pieces"]
        dark_pieces = INITIAL_POSITIONS["dark_pieces"]
        for piece in light_pieces:
            for pos in light_pieces[piece]:
                cell = pygame.Vector2(pos)
                if piece == "King":
                    self.grid[pos]["piece"] = King(pos=cell, color="light", group=self.pieces_sprites)
                if piece == "Queen":
                    self.grid[pos]["piece"] = Queen(cell, "light", self.pieces_sprites)
                if piece == "Rooks":
                    self.grid[pos]["piece"] = Rook(cell, "light", self.pieces_sprites)
                if piece == "Bishops":
                    self.grid[pos]["piece"] = Bishop(cell, "light", self.pieces_sprites)
                if piece == "Knights":
                    self.grid[pos]["piece"] = Knight(cell, "light", self.pieces_sprites)
                if piece == "Pawns":
                    self.grid[pos]["piece"] = Pawn(cell, "light", self.pieces_sprites)

        for piece in dark_pieces:
            for pos in dark_pieces[piece]:
                cell = pygame.Vector2(pos)
                if piece == "King":
                    self.grid[pos]["piece"] = King(pos=cell, color="dark", group=self.pieces_sprites)
                if piece == "Queen":
                    self.grid[pos]["piece"] = Queen(cell, "dark", self.pieces_sprites)
                if piece == "Rooks":
                    self.grid[pos]["piece"] = Rook(cell, "dark", self.pieces_sprites)
                if piece == "Bishops":
                    self.grid[pos]["piece"] = Bishop(cell, "dark", self.pieces_sprites)
                if piece == "Knights":
                    self.grid[pos]["piece"] = Knight(cell, "dark", self.pieces_sprites)
                if piece == "Pawns":
                    self.grid[pos]["piece"] = Pawn(cell, "dark", self.pieces_sprites)

        # self.grid[(4, 0)]["piece"] = King(pygame.Vector2(4, 0), "light", self.pieces_sprites)
        # self.grid[(4, 7)]["piece"] = King(pygame.Vector2(4, 7), "dark", self.pieces_sprites)
        #
        # self.grid[(3, 0)]["piece"] = Queen(pygame.Vector2(3, 0), "light", self.pieces_sprites)
        # self.grid[(3, 7)]["piece"] = Queen(pygame.Vector2(3, 7), "dark", self.pieces_sprites)
        # self.grid[(0, 0)]["piece"] = Rook(pygame.Vector2(0, 0), "light", self.pieces_sprites)
        # self.grid[(0, 7)]["piece"] = Rook(pygame.Vector2(0, 7), "dark", self.pieces_sprites)
        # self.grid[(7, 0)]["piece"] = Rook(pygame.Vector2(7, 0), "light", self.pieces_sprites)
        # self.grid[(7, 7)]["piece"] = Rook(pygame.Vector2(7, 7), "dark", self.pieces_sprites)
        # self.grid[(2, 0)]["piece"] = Bishop(pygame.Vector2(2, 0), "light", self.pieces_sprites)
        # self.grid[(2, 7)]["piece"] = Bishop(pygame.Vector2(2, 7), "dark", self.pieces_sprites)
        # self.grid[(5, 0)]["piece"] = Bishop(pygame.Vector2(5, 0), "light", self.pieces_sprites)
        # self.grid[(5, 7)]["piece"] = Bishop(pygame.Vector2(5, 7), "dark", self.pieces_sprites)
        # self.grid[(1, 0)]["piece"] = Knight(pygame.Vector2(1, 0), "light", self.pieces_sprites)
        # self.grid[(1, 7)]["piece"] = Knight(pygame.Vector2(1, 7), "dark", self.pieces_sprites)
        # self.grid[(6, 0)]["piece"] = Knight(pygame.Vector2(6, 0), "light", self.pieces_sprites)
        # self.grid[(6, 7)]["piece"] = Knight(pygame.Vector2(6, 7), "dark", self.pieces_sprites)
        #
        # for i in range(8):
        #     self.grid[(i, 1)]["piece"] = Pawn(pygame.Vector2(i, 1), "light", self.pieces_sprites)
        #     self.grid[(i, 6)]["piece"] = Pawn(pygame.Vector2(i, 6), "dark", self.pieces_sprites)

    def swap_colors(self):
        for pos in self.grid:
            if self.has_piece(pos):
                if self.grid[pos]["piece"].color == "dark":
                    pass

    def has_piece(self, pos):
        return self.grid[pos]["piece"]

    def update_grid(self, pos):
        self.grid[self.initial_cell]["piece"] = None
        self.grid[pos]["piece"] = self.active_piece

    def update_active_piece(self, input, dt):
        mouse_pos = pygame.mouse.get_pos()
        if input.left_button:
            if not self.active_piece:
                row_i, col_i = mouse_pos[0] // 64, mouse_pos[1] // 64
                self.initial_cell = row_i, col_i
                self.active_piece = self.has_piece((row_i, col_i))
            else:
                self.active_piece.motion(mouse_pos, dt)

        elif self.active_piece:
            row_i, col_i = mouse_pos[0] // 64, mouse_pos[1] // 64
            if self.has_piece((row_i, col_i)):
                self.active_piece.rect.topleft = (self.initial_cell[0] * 64, self.initial_cell[1] * 64)
            else:
                self.update_grid((row_i, col_i))
                self.active_piece.rect.topleft = row_i * 64, col_i * 64
            self.active_piece = None

    def update(self, input, dt):
        if input.swap:
            self.swap_colors()
        self.update_active_piece(input, dt)

    def draw(self):
        for pos in self.grid:
            color = self.grid[pos]["color"]
            pygame.draw.rect(self.screen, color, [pos[0] * self.CELL_SIZE, pos[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE])
            if self.has_piece(pos):
                pygame.draw.rect(self.screen, (255, 0, 0), [pos[0] * self.CELL_SIZE, pos[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE], 2)

        for piece in self.pieces_sprites:
            piece.custom_draw()

        #self.pieces_sprites.draw(self.screen)



