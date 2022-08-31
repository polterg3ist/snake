import pygame
import controls
from field import Field
from snake import Snake


def main():
    pygame.init()
    FPS = 10
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake")
    field = Field(screen)
    field.create()
    snake = Snake(field)

    while True:
        clock.tick(FPS)
        controls.events(snake)
        controls.update(screen, field, snake)


if __name__ == "__main__":
    main()