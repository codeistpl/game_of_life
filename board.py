import pygame
from math import floor
from colors import *


class Board:
    def __init__(self, surf, size, color=(0, 0, 0)):
        self.size = size
        self.surf = surf
        self.step = (surf.get_size()[0] / self.size[0], surf.get_size()[1] / self.size[1])
        self.color = color


    def draw(self):
        self._draw_matrix(self.size)

    def get_idx(self, pos):
        return floor(pos[0] / self.step[0]), floor(pos[1] / self.step[1])


    def draw_city(self, idx):
        pygame.draw.rect(self.surf, self.color, self._get_rect(idx))

    def clear_city(self, idx):
        pygame.draw.rect(self.surf, (0,0,0), self._get_rect(idx))

    def _get_rect(self, idx):
        rect = pygame.Rect(idx[0]*self.step[0]+1, idx[1]*self.step[1]+1, self.step[0]-1, self.step[1]-1)
        return rect

    def _draw_columns(self, number):
        step = self.surf.get_width() / number
        for i in range(number):
            pygame.draw.line(self.surf, GREY, (step * i, 0), (step * i, self.surf.get_width()))

    def _draw_rows(self, number):
        step = self.surf.get_width() / number
        for i in range(number):
            pygame.draw.line(self.surf, GREY, (0, step * i), (self.surf.get_height(), step * i))

    def _draw_matrix(self, size):
        self._draw_columns(size[0])
        self._draw_rows(size[1])

    def get_surrounding(self, idx):
        idxs = []
        for col in range(-1, 2):
            for row in range(-1, 2):
                idxs.append((idx[0] + col, idx[1] + row))
        idxs.remove(idx)
        return [idx for idx in idxs if 0 <= idx[0] < self.size[0] and 0 <= idx[1] < self.size[1]]

