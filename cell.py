import pygame


class Cell:
    def __init__(self, screen, posx, posy):
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.cell_surf = pygame.Surface((20, 20))
        self.rect = self.cell_surf.get_rect()
        self.is_snake = False
        self.is_food = False

    def output(self):
        self.screen.blit(self.cell_surf, (self.posx, self.posy))

        if self.is_snake:
            self.cell_surf.fill((0, 255, 0))

        elif self.is_food:
            self.cell_surf.fill((255, 0, 0))

        else:
            self.cell_surf.fill((0, 0, 111))
