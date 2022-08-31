import pygame
from sys import exit as close_game


def events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not snake.snakeMove_down:
                if not snake.field.field[snake.snake_moves[0][0][0] - 1][snake.snake_moves[0][0][1]].is_snake:
                    snake.last_key = "w"
                snake.snakeMove_up, snake.snakeMove_down, snake.snakeMove_right, snake.snakeMove_left = (
                    True, False, False, False)

            elif event.key == pygame.K_s and not snake.snakeMove_up:
                if not snake.field.field[snake.snake_moves[0][0][0] + 1][snake.snake_moves[0][0][1]].is_snake:
                    snake.last_key = "s"
                snake.snakeMove_up, snake.snakeMove_down, snake.snakeMove_right, snake.snakeMove_left = (
                    False, True, False, False)
            elif event.key == pygame.K_a and not snake.snakeMove_right:
                if not snake.field.field[snake.snake_moves[0][0][0]][snake.snake_moves[0][0][1]-1].is_snake:
                    snake.last_key = "a"
                snake.snakeMove_up, snake.snakeMove_down, snake.snakeMove_right, snake.snakeMove_left = (
                    False, False, False, True)
            elif event.key == pygame.K_d and not snake.snakeMove_left:
                if not snake.field.field[snake.snake_moves[0][0][0]][snake.snake_moves[0][0][1]+1].is_snake:
                    snake.last_key = "d"
                snake.snakeMove_up, snake.snakeMove_down, snake.snakeMove_right, snake.snakeMove_left = (
                    False, False, True, False)



def update(screen, field, snake):
    screen.fill((0, 0, 0))
    snake.update()
    field.update()
    pygame.display.flip()
