import pygame
import time
from source.base import Base
from board import Board


class Game(Base):
    def initialize(self):
        self.board = Board()

    def update(self):
        dt = self.clock.get_time() / 1000
        #self.input.update(self.board, dt)
        #print(f"MOTION: {self.input.mouse_motion}\tLEFT_BUTTON: {self.input.left_button}")
        self.board.update(self.input, dt)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.board.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
