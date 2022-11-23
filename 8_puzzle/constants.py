WINDOW_EXTENT = 640
WINDOW_HEIGHT = 480
BOARD_EXTENT = BOARD_HEIGHT = 3
TILE_SIZE = 80
FPS = 30
BLANK_SPACE = None

ORANGE = (255, 115, 30)
DARK_BLUE = (24, 70, 162)
WHITE = (255, 248, 234)
LIGHT_BLUE = (95, 158, 248)
FONT_SIZE = 16

MARGIN_X = (WINDOW_EXTENT - TILE_SIZE * BOARD_EXTENT + BOARD_EXTENT - 1) // 2
MARGIN_Y = (WINDOW_HEIGHT - TILE_SIZE * BOARD_HEIGHT + BOARD_HEIGHT - 1) // 2

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

SOLVED = 'SOLVED!'
INSTRUCTION = 'CLICK A TILE OR PRESS THE ARROW OR WASD KEYS TO SLIDE.'
GENERATING = 'GENERATING A SHUFFLED PUZZLE...'
SOLVING = 'SOLVING...'
