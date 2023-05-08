import pygame


class Input:

    def __init__(self):
        self.left_button_was_clicked = False
        self.right_button = False
        self.quit = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.left_button_was_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.left_button_was_clicked = False
