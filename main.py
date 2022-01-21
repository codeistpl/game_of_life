import time

import pygame
from pygame.locals import *
from board import Board
from city import City
from colors import *
from game_thread import GameThread

surf = pygame.display.set_mode((600, 600))
surf.fill(BLACK)
pygame.display.set_caption("Game of life")
game_size = (30, 30)


def on_click(cities, board):
    pos = pygame.mouse.get_pos()
    idx = board.get_idx(pos)
    cities[idx].toggle()
    cities[idx].draw()


def on_time(cities, board):
    for city in cities.values():
        count = count_active_cities(board.get_surrounding(city.idx), cities)
        if not city.state and count == 3:
            city.toggle()
        elif city.state and (count < 2 or count > 3):
            city.toggle()
        city.draw()


def game_refresh(cities, break_loop):
    while not break_loop:
        on_time(cities)
        time.sleep(1)


def count_active_cities(idxs, cities):
    counter = 0
    for idx in idxs:
        if cities[idx].state:
            counter += 1
    return counter


def make_cities(board):
    cities = {}
    for row in range(game_size[0]):
        for col in range(game_size[1]):
            idx = (row, col)
            cities[idx] = City(board, idx)
            cities[idx].draw()
    return cities


def main():
    break_loop = False
    board = Board(surf, game_size, RED)
    board.draw()
    cities = make_cities(board)
    game_ticking = GameThread(target=on_time, args=(cities, board))
    game_ticking.start()

    while not break_loop:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                game_ticking.stop()
                break_loop = True

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 == left button
                    on_click(cities, board)

    game_ticking.join()


if __name__ == '__main__':
    main()
