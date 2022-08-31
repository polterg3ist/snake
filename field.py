import pygame
from cell import Cell


class Field:
    def __init__(self, screen):
        self.screen = screen
        self.field = []

    def create(self):
        for line in range(21):
            field_line = []
            for row in range(21):
                x = 30 * row
                y = 30 * line
                cell = Cell(self.screen, x, y)
                field_line.append(cell)
            self.field.append(field_line)

    def update(self):
        for line in self.field:
            for cell in line:
                cell.output()
