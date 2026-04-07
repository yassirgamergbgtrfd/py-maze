# 🎮 MAZE EXPLORER - Student Edition

> **Educational Project** - This is a "80% complete" game. The core engine is ready, but the player movement, shooting logic, and collision detection are left for **you** to build!

Welcome to the Maze Explorer! This project is designed to help you bridge the gap between "filling in the gaps" and building your own software. You have the skeleton—now give it a brain.

---

## 📋 Table of Contents

1. [Setup Instructions](#-setup-instructions)
2. [Your Mission (The TODOs)](#-your-mission-the-todos)
3. [The Level Designer](#-the-level-designer)
4. [Customization Guide](#-customization-guide)
5. [Troubleshooting](#-troubleshooting)

---

## 🚀 Setup Instructions

### Step 1: Install Pygame
Open your **Terminal** or **Command Prompt** and run:
```bash
pip install pygame
```

### Step 2: Run the Game
Open the `maze_game.py` file in your editor and run it. 
*Note: The game will open, but you won't be able to move yet! That's your first task.*

---

## 🛠 Your Mission (The TODOs)

Open `maze_game.py` and search for the `STUDENT TODO` comments. You must complete these 5 challenges:

1.  **TODO 1: Player Movement** - Use `pygame.key.get_pressed()` to make the blue square move.
2.  **TODO 2: Shooting** - Create a new `Bullet` instance when the **Spacebar** is pressed.
3.  **TODO 3: Bullet Collisions** - Make the enemies disappear when they get hit by a bullet.
4.  **TODO 4: Player Damage** - If an enemy touches you, teleport back to the start!
5.  **TODO 5: Win Condition** - Detect when the player reaches the green goal.

---

## 🗺 The Level Designer

You can change the entire layout of the game without writing complex code! Find the `level_map` list:

- **"W"** = Wall (White)
- **"P"** = Player Starting Position
- **"E"** = Enemy (Red)
- **"G"** = Goal (Green)
- **" "** = Empty space (Walkable)

**Example Custom Maze:**
```python
level_map = [
    "WWWWWWWWWW",
    "WP      EW",
    "W  WWWW  W",
    "W  E    GW",
    "WWWWWWWWWW",
]
```

---

## 🎨 Customization Guide

### 1. Change Colors
Look at the top of the file under the `COLORS` section. Try changing the RGB values:
- **Red:** `(255, 0, 0)`
- **Green:** `(0, 255, 0)`
- **Gold:** `(255, 215, 0)`

### 2. Adjust Difficulty
Inside the `Player`, `Enemy`, or `Bullet` classes, look for `self.speed`.
- Increase `self.speed` in the `Enemy` class to make the game harder.
- Decrease `self.speed` in the `Bullet` class to make shooting a challenge.

### 3. Graphics (Pro Challenge)
Instead of `self.image.fill(COLOR)`, try loading an actual image:
```python
self.image = pygame.image.load("my_character.png")
self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
```

---

## 🔧 Troubleshooting

### "The player goes through walls!"
Check **TODO 1**. Ensure you are using the provided `old_x` and `old_y` logic. If the player moves into a wall, the code should "undo" that move.

### "I press Space but no bullets appear."
Did you remember to add the bullet to `all_sprites`?
```python
all_sprites.add(new_bullet)
bullets.add(new_bullet)
```
If it's not in `all_sprites`, Pygame won't know it needs to be drawn on the screen!

### "The game crashes on start."
Check your `level_map`. Ensure every row has the same number of characters and that you have at least one **"P"** (Player) on the map.

---

## 🎯 Final Goal
Once you have finished all the TODOs, try to beat your own maze. If it's too easy, add more enemies (**E**) or make the paths narrower!

**Happy coding! 🚀**
