import random
from collections import namedtuple

from constants import *


class Puzzle(namedtuple('Puzzle', ['board', 'dimension', 'zero'])):
    __slots__ = ()

    def __new__(cls, board, dimension, zero=None):
        if zero is None:
            zero = board.index(0)

        return super().__new__(cls, board, dimension, zero)

    def solved(self):
        return self.board == tuple(range(self.dimension**2))

    def actions(self):
        at = self.zero

        if at >= self.dimension:
            yield self._move(at - self.dimension)
        if at < self.dimension * 2:
            yield self._move(at + self.dimension)
        if at % self.dimension:
            yield self._move(at - 1)
        if (at + 1) % self.dimension:
            yield self._move(at + 1)

    def _move(self, to):
        board = list(self.board)
        board[self.zero], board[to] = board[to], board[self.zero]

        return Puzzle(tuple(board), self.dimension, to)

    def manhattan(self):
        distance = 0
        for digit in range(1, self.dimension**2):
            index = self.board.index(digit)
            x, y = divmod(digit, 3)
            i, j = divmod(index, 3)
            distance += abs(x - i) + abs(y - j)
        return distance

    def shuffle(self):
        puzzle = self
        for _ in range(80):
            puzzle = random.choice(list(puzzle.actions()))
        return puzzle


class Node(namedtuple('Node', ['puzzle', 'parent'])):
    def __new__(cls, puzzle, parent=None):
        self = super().__new__(cls, puzzle, parent)
        self.g = parent.g + 1 if parent is not None else 0

        return self

    @property
    def f(self):
        return self.g + self.h

    @property
    def h(self):
        return self.puzzle.manhattan()

    @property
    def action(self):
        if self.parent is None:
            return None

        directions = {
            -self.puzzle.dimension: UP,
            +self.puzzle.dimension: DOWN,
            -1: LEFT,
            +1: RIGHT
        }

        return directions[self.puzzle.zero - self.parent.puzzle.zero]
