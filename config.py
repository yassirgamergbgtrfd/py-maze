# ============================================================================
# GAME CONFIGURATION FILE
# ============================================================================
# This file contains all the customizable settings for the Maze Game.
# Students can modify these values to customize their game!
# ============================================================================

# INTENTIONAL LEARNING POINT: Try changing these values to customize your game!

# ============================================================================
# SCREEN SETTINGS
# ============================================================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (135, 206, 235)  # Light blue background (RGB format)

# ============================================================================
# GAME SPEED SETTINGS
# ============================================================================
# NOTE: Higher values = faster movement
PLAYER_SPEED = 5
ENEMY_SPEED = 3
FPS = 60  # Frames per second

# ============================================================================
# COLORS (RGB Format: Red, Green, Blue) - Values from 0-255
# ============================================================================
# Try changing these to give your game a unique look!
COLOR_PLAYER = (255, 255, 0)      # Yellow (Like Pac-Man!)
COLOR_WALL = (200, 200, 200)      # Light gray
COLOR_ENEMY1 = (0, 0, 255)        # Blue
COLOR_ENEMY2 = (128, 64, 128)     # Purple
COLOR_COIN = (255, 215, 0)        # Gold
COLOR_TEXT = (0, 0, 0)            # Black

# ============================================================================
# GAME OBJECTS SIZES
# ============================================================================
PLAYER_SIZE = 20
ENEMY_SIZE = 20
WALL_THICKNESS = 20
COIN_SIZE = 5

# ============================================================================
# MAZE LAYOUT
# ============================================================================
# '0' = Empty space, '1' = Wall
# You can create your own maze! Just make sure the grid is rectangular.
# LEARNING POINT: Try designing your own maze layout!

MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# ============================================================================
# STARTING POSITIONS
# ============================================================================
# These are (row, column) positions in the maze
PLAYER_START_ROW = 1
PLAYER_START_COL = 1

ENEMY1_START_ROW = 1
ENEMY1_START_COL = 18

ENEMY2_START_ROW = 13
ENEMY2_START_COL = 1

# ============================================================================
# GAME RULES
# ============================================================================
COINS_TO_WIN = 50  # How many coins the player needs to collect to win
MAX_HEALTH = 3     # How many times the player can be hit
