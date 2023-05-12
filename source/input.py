import pygame


class Input:

    def __init__(self):
        self.left_button = False
        self.right_button = False
        self.mouse_motion = False
        self.quit = False
        self.swap = False

        self.current_event = None

    def update(self):

        for event in pygame.event.get():
            self.current_event = event
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #self.quit = True
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_SPACE:
                    self.swap = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.swap = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.left_button = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.left_button = False







