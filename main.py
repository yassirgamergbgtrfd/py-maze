import pygame
import sys

# ==========================================
# 1. INITIALIZATION & CONSTANTS
# ==========================================
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
FPS = 60

# Colors (Students can change these!)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Explorer - Yassir Edition")
clock = pygame.time.Clock()

# ==========================================
# 2. SPRITE CLASSES
# ==========================================
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # To use an image later: self.image = pygame.image.load("player.png")
        self.image = pygame.Surface((TILE_SIZE - 10, TILE_SIZE - 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        # Save starting position for when the player dies
        self.start_x = x * TILE_SIZE + 5
        self.start_y = y * TILE_SIZE + 5
        self.rect.x = self.start_x
        self.rect.y = self.start_y

        self.speed = 5
        self.facing = "RIGHT" # Helps bullets know which way to go

    def update(self, walls):
        # Save old position in case we hit a wall
        old_x = self.rect.x
        old_y = self.rect.y

        keys = pygame.key.get_pressed()

        # ==========================================
        # STUDENT TODO 1: PLAYER MOVEMENT
        # ==========================================
        # Hint: If the left arrow key is pressed (pygame.K_LEFT),
        # decrease self.rect.x by self.speed and set self.facing to "LEFT".
        # Do the same for RIGHT, UP, and DOWN!

        # [WRITE YOUR MOVEMENT CODE HERE]



        # --- Wall Collision Logic (Provided so you don't get stuck!) ---
        # If the player hits a wall after moving, we push them back to their old position.
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.rect.x = old_x
                self.rect.y = old_y

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 10, TILE_SIZE - 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE + 5
        self.rect.y = y * TILE_SIZE + 5
        self.move_timer = 0
        self.direction = 1

    def update(self):
        # Simple enemy movement: wobble back and forth
        self.move_timer += 1
        if self.move_timer > 30:
            self.direction *= -1
            self.move_timer = 0
        self.rect.y += self.direction * 2

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10
        self.direction = direction

    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed

        # Kill bullet if it goes off screen to save memory
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

# ==========================================
# 3. LEVEL DESIGN (Highly Customizable)
# ==========================================
# W = Wall, P = Player Start, E = Enemy, G = Goal, Space = Empty
level_map = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WP       W         W",
    "W        W    E    W",
    "W   WWWWWW         W",
    "W        W    WWWWWW",
    "W  E               W",
    "W        W         W",
    "W  WWWWWWWWWWWW    W",
    "W             E    W",
    "W        W         W",
    "W        W         G",
    "WWWWWWWWWWWWWWWWWWWW",
]

# Sprite Groups
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
goals = pygame.sprite.Group()

player = None

# Parse the level map
for row_index, row in enumerate(level_map):
    for col_index, char in enumerate(row):
        if char == "W":
            wall = Wall(col_index, row_index)
            all_sprites.add(wall)
            walls.add(wall)
        elif char == "P":
            player = Player(col_index, row_index)
            all_sprites.add(player)
        elif char == "E":
            enemy = Enemy(col_index, row_index)
            all_sprites.add(enemy)
            enemies.add(enemy)
        elif char == "G":
            goal = Goal(col_index, row_index)
            all_sprites.add(goal)
            goals.add(goal)

# ==========================================
# 4. MAIN GAME LOOP
# ==========================================
running = True
while running:
    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # ==========================================
                # STUDENT TODO 2: SHOOTING
                # ==========================================
                # When SPACE is pressed, create a Bullet object.
                # Pass it the player's center x, center y, and facing direction.
                # Add the new bullet to 'all_sprites' and 'bullets' groups.

                # [WRITE YOUR SHOOTING CODE HERE]
                pass

    # --- Updates ---
    # Update player (passing walls for collision check)
    player.update(walls)

    # Update other sprites
    enemies.update()
    bullets.update()

    # ==========================================
    # STUDENT TODO 3: BULLET VS ENEMY COLLISION
    # ==========================================
    # Hint: Use pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
    # If a bullet hits an enemy, BOTH should disappear (dokill=True).

    # [WRITE YOUR BULLET COLLISION CODE HERE]


    # ==========================================
    # STUDENT TODO 4: PLAYER VS ENEMY COLLISION
    # ==========================================
    # Hint: Use pygame.sprite.spritecollide(sprite, group, dokill)
    # If the player hits an enemy, teleport the player back to player.start_x and player.start_y.

    # [WRITE YOUR ENEMY COLLISION CODE HERE]


    # ==========================================
    # STUDENT TODO 5: WIN CONDITION (PLAYER VS GOAL)
    # ==========================================
    # If the player collides with the goal, print "YOU WIN!" to the console and set running = False

    # [WRITE YOUR WIN CONDITION CODE HERE]


    # --- Drawing ---
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
