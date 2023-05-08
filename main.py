import pygame
import time
from source.base import Base
from board import Board


class Game(Base):
    def initialize(self):
        self.board = Board()

    def update(self):
        #print(pygame.time.get_ticks() // 1000)
        self.board.update(self.input.left_button_was_clicked)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.board.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
