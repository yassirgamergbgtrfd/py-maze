# ============================================================================
# GAME ENTITIES
# ============================================================================
# This module contains all the game objects (Player, Enemies, Coins)
# Each object is a class with its own properties and methods
# ============================================================================

import pygame
from config import *

class Player:
    """
    The Player class represents the character controlled by the user.
    
    Attributes:
        x (int): X position on screen
        y (int): Y position on screen
        speed (int): How fast the player moves
        radius (int): Size of the player (for collision detection)
        color (tuple): RGB color of the player
    """
    
    def __init__(self, start_row, start_col):
        """
        Initialize the player at a starting position.
        
        Args:
            start_row (int): Starting row in the maze
            start_col (int): Starting column in the maze
        """
        # Convert maze grid position to pixel position
        self.grid_row = start_row
        self.grid_col = start_col
        self.x = start_col * WALL_THICKNESS
        self.y = start_row * WALL_THICKNESS
        
        self.speed = PLAYER_SPEED
        self.radius = PLAYER_SIZE
        self.color = COLOR_PLAYER
        self.direction_x = 0
        self.direction_y = 0
        self.coins_collected = 0
        self.health = MAX_HEALTH
    
    def update_position(self, maze):
        """
        Update player position based on input direction.
        Check collision with walls.
        
        Args:
            maze (list): 2D list representing the maze layout
        """
        # Calculate new position
        new_x = self.x + (self.direction_x * self.speed)
        new_y = self.y + (self.direction_y * self.speed)
        
        # Check if new position is valid (not hitting a wall)
        if self._is_valid_position(new_x, new_y, maze):
            self.x = new_x
            self.y = new_y
            
            # Update grid position
            self.grid_col = self.x // WALL_THICKNESS
            self.grid_row = self.y // WALL_THICKNESS
    
    def _is_valid_position(self, x, y, maze):
        """
        Check if a position is valid (within bounds and not in a wall).
        
        INTENTIONAL LEARNING POINT: This method has a subtle bug!
        See if you can find it and fix it. Hint: What happens at the edges?
        
        Args:
            x (int): X position to check
            y (int): Y position to check
            maze (list): 2D list representing the maze
            
        Returns:
            bool: True if position is valid, False otherwise
        """
        # Convert pixel position to grid position
        col = int(x // WALL_THICKNESS)
        row = int(y // WALL_THICKNESS)
        
        # Check if position is within maze bounds
        if row < 0 or col < 0:
            return False
        if row >= len(maze) or col >= len(maze[0]):
            return False
        
        # Check if position is not a wall
        if maze[row][col] == 1:
            return False
        
        return True
    
    def draw(self, screen):
        """
        Draw the player on the screen.
        
        Args:
            screen (pygame.Surface): The game screen to draw on
        """
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def set_direction(self, direction_x, direction_y):
        """
        Set the player's movement direction.
        
        Args:
            direction_x (int): Horizontal direction (-1, 0, or 1)
            direction_y (int): Vertical direction (-1, 0, or 1)
        """
        self.direction_x = direction_x
        self.direction_y = direction_y


class Enemy:
    """
    The Enemy class represents an AI-controlled character that chases the player.
    
    Attributes:
        x (int): X position on screen
        y (int): Y position on screen
        speed (int): How fast the enemy moves
        color (tuple): RGB color of the enemy
    """
    
    def __init__(self, start_row, start_col, color):
        """
        Initialize an enemy at a starting position.
        
        Args:
            start_row (int): Starting row in the maze
            start_col (int): Starting column in the maze
            color (tuple): RGB color for this enemy
        """
        self.grid_row = start_row
        self.grid_col = start_col
        self.x = start_col * WALL_THICKNESS
        self.y = start_row * WALL_THICKNESS
        
        self.speed = ENEMY_SPEED
        self.color = color
        self.radius = ENEMY_SIZE
    
    def update_position(self, maze, player):
        """
        Update enemy position using simple AI (chase the player).
        
        INTENTIONAL LEARNING POINT: The AI is very basic!
        Try to improve it or add different enemy behaviors.
        
        Args:
            maze (list): 2D list representing the maze
            player (Player): The player object to chase
        """
        # Simple chase logic: move towards player
        if self.x < player.x:
            self._try_move(self.speed, 0, maze)
        elif self.x > player.x:
            self._try_move(-self.speed, 0, maze)
        
        if self.y < player.y:
            self._try_move(0, self.speed, maze)
        elif self.y > player.y:
            self._try_move(0, -self.speed, maze)
    
    def _try_move(self, delta_x, delta_y, maze):
        """
        Try to move the enemy in a direction.
        
        Args:
            delta_x (int): Change in X position
            delta_y (int): Change in Y position
            maze (list): 2D list representing the maze
        """
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        
        # Check if new position is valid
        col = int(new_x // WALL_THICKNESS)
        row = int(new_y // WALL_THICKNESS)
        
        # Check bounds and walls
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
            if maze[row][col] != 1:  # Not a wall
                self.x = new_x
                self.y = new_y
                self.grid_col = col
                self.grid_row = row
    
    def draw(self, screen):
        """
        Draw the enemy on the screen.
        
        Args:
            screen (pygame.Surface): The game screen to draw on
        """
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def check_collision(self, player):
        """
        Check if this enemy has collided with the player.
        
        Args:
            player (Player): The player object
            
        Returns:
            bool: True if collision detected, False otherwise
        """
        distance = ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5
        return distance < (self.radius + player.radius)


class Coin:
    """
    The Coin class represents collectible items in the maze.
    
    Attributes:
        x (int): X position on screen
        y (int): Y position on screen
        color (tuple): RGB color of the coin
        collected (bool): Whether the coin has been collected
    """
    
    def __init__(self, grid_row, grid_col):
        """
        Initialize a coin at a grid position.
        
        Args:
            grid_row (int): Row in the maze
            grid_col (int): Column in the maze
        """
        self.grid_row = grid_row
        self.grid_col = grid_col
        self.x = grid_col * WALL_THICKNESS + WALL_THICKNESS // 2
        self.y = grid_row * WALL_THICKNESS + WALL_THICKNESS // 2
        
        self.color = COLOR_COIN
        self.radius = COIN_SIZE
        self.collected = False
    
    def draw(self, screen):
        """
        Draw the coin on the screen (only if not collected).
        
        Args:
            screen (pygame.Surface): The game screen to draw on
        """
        if not self.collected:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def check_collision(self, player):
        """
        Check if the player has collected this coin.
        
        Args:
            player (Player): The player object
            
        Returns:
            bool: True if collected, False otherwise
        """
        distance = ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5
        if distance < (self.radius + player.radius):
            self.collected = True
            return True
        return False
