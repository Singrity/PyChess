import sys
import pygame
from source.input import Input


class Base:

    def __init__(self, screen_size=None):
        pygame.init()
        if not screen_size:
            screen_size = [512, 512]

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Chess")
        self.running = True
        self.clock = pygame.time.Clock()
        self.input = Input()

    def initialize(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        # startup
        self.initialize()

        # main loop
        while self.running:
            # process input
            self.input.update()
            if self.input.quit:
                self.running = False
            # update
            self.update()

            # render
            self.render()
            # display image on screen
            pygame.display.flip()

            # pause if necessary to achieve 60 FPS
            self.clock.tick(60)

        # shutdown
        pygame.quit()
        sys.exit()