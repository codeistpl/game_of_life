from board import Board


class City:
    def __init__(self, board: Board, idx):
        self.board = board
        self.idx = idx
        self.state = False

    def toggle(self):
        self.state = not self.state

    def draw(self):
        if self.state:
            self.board.draw_city(self.idx)
        else:
            self.board.clear_city(self.idx)
