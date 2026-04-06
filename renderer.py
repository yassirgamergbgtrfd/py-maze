# ============================================================================
# MAZE RENDERER
# ============================================================================
# This module handles drawing the maze and game UI elements to the screen
# ============================================================================

import pygame
from config import *

class MazeRenderer:
    """
    The MazeRenderer class handles all visual rendering of the game.
    
    Attributes:
        screen (pygame.Surface): The game window
        font_large (pygame.font.Font): Font for large text
        font_small (pygame.font.Font): Font for small text
    """
    
    def __init__(self, screen):
        """
        Initialize the renderer.
        
        Args:
            screen (pygame.Surface): The pygame game screen
        """
        self.screen = screen
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw_maze(self, maze):
        """
        Draw the maze walls on the screen.
        
        Args:
            maze (list): 2D list where 1 = wall, 0 = empty space
        """
        for row_index, row in enumerate(maze):
            for col_index, cell in enumerate(row):
                if cell == 1:  # This is a wall
                    x = col_index * WALL_THICKNESS
                    y = row_index * WALL_THICKNESS
                    pygame.draw.rect(
                        self.screen,
                        COLOR_WALL,
                        (x, y, WALL_THICKNESS, WALL_THICKNESS)
                    )
    
    def draw_ui(self, player, enemies):
        """
        Draw the game user interface (health, coins, score).
        
        Args:
            player (Player): The player object
            enemies (list): List of enemy objects
        """
        # Draw health bar
        health_text = self.font_small.render(
            f"Health: {player.health}/{MAX_HEALTH}",
            True,
            COLOR_TEXT
        )
        self.screen.blit(health_text, (10, 10))
        
        # Draw coins collected
        coins_text = self.font_small.render(
            f"Coins: {player.coins_collected}",
            True,
            COLOR_TEXT
        )
        self.screen.blit(coins_text, (10, 40))
        
        # Draw goal
        goal_text = self.font_small.render(
            f"Goal: {COINS_TO_WIN} coins",
            True,
            COLOR_TEXT
        )
        self.screen.blit(goal_text, (10, 70))
    
    def draw_game_over_screen(self, player, won):
        """
        Draw the game over screen (win or lose).
        
        INTENTIONAL LEARNING POINT: See what happens when you change
        the text or colors here! You could make your own victory screen.
        
        Args:
            player (Player): The player object
            won (bool): True if player won, False if lost
        """
        # Create a semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        if won:
            # Victory screen
            title_text = self.font_large.render(
                "YOU WIN!",
                True,
                (0, 255, 0)  # Green
            )
            subtitle_text = self.font_small.render(
                f"You collected {player.coins_collected} coins!",
                True,
                (255, 255, 255)  # White
            )
        else:
            # Game over screen
            title_text = self.font_large.render(
                "GAME OVER",
                True,
                (255, 0, 0)  # Red
            )
            subtitle_text = self.font_small.render(
                f"You collected {player.coins_collected} coins",
                True,
                (255, 255, 255)  # White
            )
        
        # Draw text in center of screen
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        )
        subtitle_rect = subtitle_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        
        self.screen.blit(title_text, title_rect)
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Instructions
        restart_text = self.font_small.render(
            "Close the window to exit",
            True,
            (200, 200, 200)
        )
        restart_rect = restart_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        )
        self.screen.blit(restart_text, restart_rect)
