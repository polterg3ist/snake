import pygame
from random import randint
from sys import exit


class Snake:
    def __init__(self, field):
        self.field = field
        self.snake_moves = [[[randint(0, 14), randint(0, 14)], []]]
        #self.snake_moves = [[[5, 5], []], [[5, 4], []], [[5, 3], []]]
        #self.snake_moves = [[[6, 5+x], []] for x in range(1, 2)]
        self.snakeMove_up = False
        self.snakeMove_down = False
        self.snakeMove_left = True
        self.snakeMove_right = False
        self.last_key = None
        print(self.snake_moves)

    def snake_move(self):
        print(f"{(self.snakeMove_up, self.snakeMove_down, self.snakeMove_right, self.snakeMove_left)}")
        self.move_body()
        if self.snakeMove_up:
            if self.field.field[self.snake_moves[0][0][0] - 1][self.snake_moves[0][0][1]].is_snake:
                if self.last_key == "d":
                    self.snake_moves[0][0][1] += 1
                elif self.last_key == "a":
                    self.snake_moves[0][0][1] -= 1
            else:
                self.snake_moves[0][0][0] -= 1
            #else:
            #    print("LOSE at move up")
            #    exit()

        elif self.snakeMove_down:
            #self.snake_moves[0][1] = self.snake_moves[0][0].copy()
            #if new < 20:
            if self.field.field[self.snake_moves[0][0][0] + 1][self.snake_moves[0][0][1]].is_snake:
                if self.last_key == "d":
                    self.snake_moves[0][0][1] += 1
                elif self.last_key == "a":
                    self.snake_moves[0][0][1] -= 1
            else:
                self.snake_moves[0][0][0] += 1
            #else:
            #    #print("LOSE")
            #    print("LOSE at move down")
            #    exit()

        elif self.snakeMove_left:
            #self.snake_moves[0][1] = self.snake_moves[0][0].copy()
            #if new > -1:
            if self.field.field[self.snake_moves[0][0][0]][self.snake_moves[0][0][1] - 1].is_snake:
                if self.last_key == "w":
                    self.snake_moves[0][0][0] -= 1
                elif self.last_key == "s":
                    self.snake_moves[0][0][0] += 1
            else:
                self.snake_moves[0][0][1] -= 1
            #else:
            #    #print("LOSE")
            #    print("LOSE at move left")
            #    exit()

        elif self.snakeMove_right:
            #self.snake_moves[0][1] = self.snake_moves[0][0].copy()
            #if new < 20:
            if self.field.field[self.snake_moves[0][0][0]][self.snake_moves[0][0][1] + 1].is_snake:
                if self.last_key == "w":
                    self.snake_moves[0][0][0] -= 1
                elif self.last_key == "s":
                    self.snake_moves[0][0][0] += 1
            else:
                self.snake_moves[0][0][1] += 1
            #else:
            #    #print("LOSE")
            #    print(f"LOSE at move right {new}")
            #    exit()


    def update(self):
        self.snake_move()
        for snake_part in self.snake_moves:
            print(snake_part, self.snake_moves, snake_part[0][0], snake_part[0][1])
            if snake_part[0][0] > 19 or snake_part[0][0] < 0:
                print('LOSE out of top or bot')
                exit()
            elif snake_part[0][1] > 19 or snake_part[0][1] < 0:
                print("LOSE out of left or right")
                exit()
            else:
                cell_of_move = self.field.field[snake_part[0][0]][snake_part[0][1]]
                if cell_of_move.is_snake:
                    print("LOSE you ate yourself :<")
                    exit()
                else:
                    cell_of_move.is_snake = True
                if snake_part[1]:
                    self.field.field[snake_part[1][0]][snake_part[1][1]].is_snake = False


    def move_body(self):
        if len(self.snake_moves) > 1:
            for ind in range(len(self.snake_moves)):
                self.snake_moves[ind][1] = self.snake_moves[ind][0].copy()
                print("#"*8)
                if ind > 0:
                    self.snake_moves[ind][0] = self.snake_moves[ind-1][1].copy()
            print(f"SNKMVS: {self.snake_moves}")



