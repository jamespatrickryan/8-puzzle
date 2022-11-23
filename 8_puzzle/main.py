import random
import sys

import pygame
from pygame.locals import *

from constants import *
from puzzle import Puzzle
from search import a_star, bfs


class PyPuzzle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('8-Puzzle')

        self.fps_clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((WINDOW_EXTENT, WINDOW_HEIGHT))
        self.font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

        text = self.pen_a_text('NEW GAME', WINDOW_EXTENT - 128, WINDOW_HEIGHT - 90)
        self.new_game_surface, self.new_game_rectangle = text

        text = self.pen_a_text('SOLVE VIA A*', WINDOW_EXTENT - 128, WINDOW_HEIGHT - 60)
        self.a_star_surface, self.a_star_rectangle = text

        text = self.pen_a_text('SOLVE VIA BFS', WINDOW_EXTENT - 128, WINDOW_HEIGHT - 30)
        self.bfs_surface, self.bfs_rectangle = text

        self.board = self.puzzle_factory(80)
        self.main_loop()

    def main_loop(self):
        while True:
            slide = None

            text = SOLVED if self.board == self.solved_puzzle else INSTRUCTION
            self.render_board(self.board, text)

            self.if_abandon()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    i, j = self.fetch_clicked_area(*event.pos)

                    if None in (i, j):
                        board = self.transformed_board()
                        puzzle = Puzzle(board, 3)

                        if self.new_game_rectangle.collidepoint(event.pos):
                            self.board = self.puzzle_factory(80)
                        elif self.a_star_rectangle.collidepoint(event.pos):
                            path = a_star(puzzle)
                            self.solve_animation(self.board, self.actions(path))
                        elif self.bfs_rectangle.collidepoint(event.pos):
                            path = bfs(puzzle)
                            self.solve_animation(self.board, self.actions(path))
                    else:
                        x, y = self.obtain_blank_indices(self.board)

                        if None:
                            ...
                        elif i == x and j == y + 1:
                            slide = UP
                        elif i == x and j == y - 1:
                            slide = DOWN
                        elif i == x + 1 and j == y:
                            slide = LEFT
                        elif i == x - 1 and j == y:
                            slide = RIGHT

                elif event.type == KEYUP:
                    if None:
                        ...
                    elif (event.key in (K_UP, K_w) and
                            self.is_a_legal_action(self.board, UP)):
                        slide = UP
                    elif (event.key in (K_DOWN, K_s) and
                            self.is_a_legal_action(self.board, DOWN)):
                        slide = DOWN
                    elif (event.key in (K_LEFT, K_a) and
                            self.is_a_legal_action(self.board, LEFT)):
                        slide = LEFT
                    elif (event.key in (K_RIGHT, K_d) and
                            self.is_a_legal_action(self.board, RIGHT)):
                        slide = RIGHT

            if slide is not None:
                self.slide_animation(self.board, slide, text, TILE_SIZE // 8)
                self.transition(self.board, slide)

            pygame.display.update()
            self.fps_clock.tick(FPS)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def if_abandon(self):
        for event in pygame.event.get(QUIT):
            self.terminate()

        for event in pygame.event.get(KEYUP):
            if event.key == K_ESCAPE:
                self.terminate()
            pygame.event.post(event)

    def transformed_board(self):
        return tuple(self.board[row][column]
                     if self.board[row][column] is not BLANK_SPACE
                     else 0
                     for column in range(BOARD_EXTENT)
                     for row in range(BOARD_HEIGHT))

    def actions(self, path):
        return [node.action
                for node in path
                if node.action is not None]

    @property
    def solved_puzzle(self):
        return [[BLANK_SPACE, 3, 6], [1, 4, 7], [2, 5, 8]]

    def obtain_blank_indices(self, board):
        for index in range(BOARD_EXTENT * BOARD_HEIGHT):
            x, y = divmod(index, 3)
            if board[x][y] is BLANK_SPACE:
                return x, y

    def transition(self, board, action):
        x, y = self.obtain_blank_indices(board)

        if None:
            ...
        elif action == UP:
            board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
        elif action == DOWN:
            board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
        elif action == LEFT:
            board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
        elif action == RIGHT:
            board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]

    def is_a_legal_action(self, board, action):
        x, y = self.obtain_blank_indices(board)

        return (
            action == UP and y != BOARD_HEIGHT - 1 or
            action == DOWN and y != 0 or
            action == LEFT and x != BOARD_EXTENT - 1 or
            action == RIGHT and x != 0
        )

    def arbitrary_action(self, board, prior):
        legal = [UP, DOWN, LEFT, RIGHT]

        if prior == UP or not self.is_a_legal_action(board, DOWN):
            legal.remove(DOWN)
        if prior == DOWN or not self.is_a_legal_action(board, UP):
            legal.remove(UP)
        if prior == LEFT or not self.is_a_legal_action(board, RIGHT):
            legal.remove(RIGHT)
        if prior == RIGHT or not self.is_a_legal_action(board, LEFT):
            legal.remove(LEFT)

        return random.choice(legal)

    def pen_a_text(self, text, head, left):
        surface = self.font.render(text, True, WHITE, ORANGE)
        rectangle = surface.get_rect()
        rectangle.topleft = head, left

        return surface, rectangle

    def left_and_head_corner(self, x, y):
        left = MARGIN_X + x * TILE_SIZE + x - 1
        head = MARGIN_Y + y * TILE_SIZE + y - 1

        return left, head

    def fetch_clicked_area(self, i, j):
        for index in range(BOARD_EXTENT * BOARD_HEIGHT):
            x, y = divmod(index, 3)
            left, head = self.left_and_head_corner(x, y)
            tile = pygame.Rect(left, head, TILE_SIZE, TILE_SIZE)
            if tile.collidepoint(i, j):
                return x, y
        else:
            return None, None

    def sketch_a_tile(self, x, y, digit, i=0, j=0):
        left, head = self.left_and_head_corner(x, y)

        left += i
        head += j

        rectangle = left, head, TILE_SIZE, TILE_SIZE

        pygame.draw.rect(self.display_surface, DARK_BLUE, rectangle)

        surface = self.font.render(str(digit), True, WHITE)
        rectangle = surface.get_rect()
        x = TILE_SIZE // 2 + left
        y = TILE_SIZE // 2 + head
        rectangle.center = x, y

        self.display_surface.blit(surface, rectangle)

    def render_board(self, board, text):
        self.display_surface.fill(ORANGE)

        text = self.pen_a_text(text, 5, 10)
        surface, rectangle = text

        self.display_surface.blit(surface, rectangle)

        for index in range(BOARD_EXTENT * BOARD_HEIGHT):
            x, y = divmod(index, 3)
            if board[x][y] is not BLANK_SPACE:
                self.sketch_a_tile(x, y, board[x][y])

        left, head = self.left_and_head_corner(0, 0)
        extent = BOARD_EXTENT * TILE_SIZE + 11
        height = BOARD_HEIGHT * TILE_SIZE + 11
        rectangle = left - 5, head - 5, extent, height

        pygame.draw.rect(self.display_surface, LIGHT_BLUE, rectangle, 4)

        self.display_surface.blit(self.new_game_surface, self.new_game_rectangle)
        self.display_surface.blit(self.a_star_surface, self.a_star_rectangle)
        self.display_surface.blit(self.bfs_surface, self.bfs_rectangle)

    def slide_animation(self, board, direction, text, animation_speed):
        x, y = self.obtain_blank_indices(board)

        if None:
            ...
        elif direction == UP:
            y += 1
        elif direction == DOWN:
            y -= 1
        elif direction == LEFT:
            x += 1
        elif direction == RIGHT:
            x -= 1

        self.render_board(board, text)

        base_surface = self.display_surface.copy()
        left, head = self.left_and_head_corner(x, y)
        rectangle = left, head, TILE_SIZE, TILE_SIZE

        pygame.draw.rect(base_surface, ORANGE, rectangle)

        for index in range(0, TILE_SIZE, animation_speed):
            self.if_abandon()

            self.display_surface.blit(base_surface, (0, 0))

            if direction == UP:
                self.sketch_a_tile(x, y, board[x][y], 0, -index)
            if direction == DOWN:
                self.sketch_a_tile(x, y, board[x][y], 0, index)
            if direction == LEFT:
                self.sketch_a_tile(x, y, board[x][y], -index, 0)
            if direction == RIGHT:
                self.sketch_a_tile(x, y, board[x][y], index, 0)

            pygame.display.update()
            self.fps_clock.tick(FPS)

    def puzzle_factory(self, slides):
        board = self.solved_puzzle
        self.render_board(board, '')

        pygame.display.update()
        pygame.time.wait(500)

        prior = None
        for _ in range(slides):
            action = self.arbitrary_action(board, prior)
            text = GENERATING
            self.slide_animation(board, action, text, TILE_SIZE // 4)
            self.transition(board, action)
            prior = action

        return board

    def solve_animation(self, board, actions):
        directions = {
            UP: DOWN,
            DOWN: UP,
            LEFT: RIGHT,
            RIGHT: LEFT
        }

        for action in actions:
            action = directions[action]
            text = SOLVING
            self.slide_animation(board, action, text, TILE_SIZE // 8)
            self.transition(board, action)


if __name__ == '__main__':
    PyPuzzle()
