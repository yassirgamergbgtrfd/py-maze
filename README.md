# 🕹️ MAZE EXPLORER - Master Edition

> **Full Version** - This is the complete, playable source code for the Pygame Maze. Use this as a reference to understand how movement, shooting, and collisions work in a real-time game loop.

This project demonstrates the core pillars of Pygame: **Sprite Groups**, **Event Handling**, **Coordinate Systems**, and **Collision Logic**.

---

## 🚀 Getting Started

1.  **Requirement**: Ensure you have Python 3.x and Pygame installed.
    ```bash
    pip install pygame
    ```
2.  **Run**: Execute the script to start the game.
    ```bash
    python maze_master.py
    ```

---

## 🎮 Controls & Mechanics

| Action | Control | Logic Behind It |
| :--- | :--- | :--- |
| **Move** | Arrow Keys | Updates `self.rect` and checks against `walls` group. |
| **Shoot** | Spacebar | Instantiates a `Bullet` at `player.rect.center`. |
| **Win** | Reach Green | Checks `spritecollide` between Player and Goal. |
| **Die** | Hit Red | Resets `player.rect` to its `start_x/y` coordinates. |

---

## 🛠️ The "Developer" Guide (How to Customize)

Now that the code is functional, you can treat this file as a **Game Engine**. Try the following modifications:

### 1. Advanced Level Editing
The `level_map` is a grid of strings. You can create massive levels or vertical towers by adding more strings to the list. 
* **Challenge**: Try to create a "Boss Room" at the end of your maze with 5+ enemies.

### 2. Tuning the Physics
In the `__init__` methods of the classes, you can find the "Balance Variables":
* `self.speed = 5` (Player): Change this to **10** for a "Sprint Mode."
* `self.direction = 1` (Enemy): Change the `2` in `self.rect.y += self.direction * 2` to a higher number to make enemies move faster.

### 3. Adding a "Lives" System
Currently, hitting an enemy just teleports you back. 
* **Logic Change**: Create a variable `self.lives = 3` in the Player class. 
* Inside the collision check, subtract 1 from `lives`. If `lives == 0`, then call `pygame.quit()`.

### 4. Sprite Graphics
Instead of solid colors, you can use images. Replace the `Surface` code in any class with:
```python
# Load the image
self.image = pygame.image.load("hero.png").convert_alpha()
# Resize it to fit the tile
self.image = pygame.transform.scale(self.image, (TILE_SIZE - 10, TILE_SIZE - 10))
```

---

## 🔍 Code Breakdown for Students

### The Sprite Group Logic
The game uses `pygame.sprite.Group()`. This is like a smart list. Instead of looping through every enemy to see if a bullet hit it, we use:
```python
pygame.sprite.groupcollide(bullets, enemies, True, True)
```
This single line handles the math for **every** bullet against **every** enemy and removes them from the game if they touch.

### Coordinate System
Remember that in Pygame, $(0,0)$ is the **Top-Left** corner. 
* Increasing `y` moves the sprite **Down**.
* Increasing `x` moves the sprite **Right**.

---

## 🔧 Troubleshooting & Common Fixes

* **Screen is Black?** Ensure `all_sprites.draw(screen)` is being called inside the `while running` loop.
* **Bullets won't fire?** Check that you added the new bullet to both `all_sprites` (for drawing) and `bullets` (for collision math).
* **Stuck in Walls?** This usually happens if the `TILE_SIZE` and the `Player.rect` size are too close. Ensure the player is slightly smaller than the tile.

---

**Congratulations on completing the Maze! What will you build next?** 🚀
