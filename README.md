# 🎮 MAZE GAME - A Customizable Pygame Project

Welcome to the Maze Game! This is a fun, interactive game where you navigate through a maze, collect coins, and avoid enemies. Best of all, **you can customize it!**

---

## 📋 Table of Contents

1. [Setup Instructions](#-setup-instructions)
2. [How to Play](#-how-to-play)
3. [Game Files](#-game-files)
4. [Customization Guide](#-customization-guide)
5. [Learning Points & Bug Challenges](#-learning-points--bug-challenges)
6. [Troubleshooting](#-troubleshooting)

---

## 🚀 Setup Instructions

### Step 1: Install Python (if not already installed)

Make sure you have Python 3.7 or higher installed on your computer.

- Check by opening **Command Prompt** (Windows) and typing:
  ```
  python --version
  ```

### Step 2: Install Pygame

In your **Command Prompt** (or Terminal), navigate to your project folder and run:

```bash
pip install -r requirements.txt
```

Or directly:

```bash
pip install pygame
```

### Step 3: Run the Game

In **Command Prompt**, type:

```bash
python main.py
```

The game window should open! 🎮

---

## 🎮 How to Play

### Controls

- **Arrow Keys**: Move up, down, left, right
- **Close Window**: Exit the game

### Objective

- **Collect Coins**: Move around the maze to collect coins (gold circles)
- **Avoid Enemies**: Don't get caught by the blue and purple enemies!
- **Reach the Goal**: Collect all 50 coins to win!

### Game Over Conditions

- **Win**: Collect enough coins (default: 50)
- **Lose**: Get hit by an enemy 3 times

---

## 📁 Game Files

Each file has a specific purpose:

| File | Purpose |
|------|---------|
| `main.py` | **START HERE** - The entry point to run the game |
| `config.py` | Game settings: colors, speeds, maze layout, coin count |
| `entities.py` | Game objects: Player, Enemy, Coin classes |
| `game.py` | Main game logic and game loop |
| `renderer.py` | Drawing and visual effects |
| `requirements.txt` | Python package dependencies |

---

## 🎨 Customization Guide

### 1. Change Colors

Open `config.py` and find the "COLORS" section. Colors use RGB format (Red, Green, Blue).

**Example:** Change the player color from yellow to red:

```python
# Before:
COLOR_PLAYER = (255, 255, 0)  # Yellow

# After:
COLOR_PLAYER = (255, 0, 0)    # Red
```

**RGB Values Cheat Sheet:**
- Red: `(255, 0, 0)`
- Green: `(0, 255, 0)`
- Blue: `(0, 0, 255)`
- Yellow: `(255, 255, 0)`
- Purple: `(128, 0, 128)`
- Orange: `(255, 165, 0)`
- White: `(255, 255, 255)`
- Black: `(0, 0, 0)`

### 2. Change Game Speed

In `config.py`, adjust:

```python
PLAYER_SPEED = 5      # Higher = faster
ENEMY_SPEED = 3       # Higher = faster
FPS = 60              # Frames per second
```

### 3. Design Your Own Maze

In `config.py`, find the `MAZE` variable:

```python
MAZE = [
    [1, 1, 1, 1, 1, ...],  # 1 = wall, 0 = empty space
    [1, 0, 0, 0, 1, ...],
    ...
]
```

- **1** = Wall (white block)
- **0** = Empty space (walkable)

Try creating a simple test maze:

```python
MAZE = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
```

### 4. Change Starting Positions

In `config.py`:

```python
PLAYER_START_ROW = 1
PLAYER_START_COL = 1

ENEMY1_START_ROW = 1
ENEMY1_START_COL = 18

ENEMY2_START_ROW = 13
ENEMY2_START_COL = 1
```

### 5. Adjust the Win Condition

In `config.py`:

```python
COINS_TO_WIN = 50  # Change this to require more or fewer coins
MAX_HEALTH = 3     # Change how many hits the player can take
```

### 6. Improve Enemy AI

Open `entities.py` and find the `Enemy.update_position()` method. The current AI is very basic:

```python
def update_position(self, maze, player):
    # Current AI just chases player
    if self.x < player.x:
        self._try_move(self.speed, 0, maze)
    ...
```

**Challenge:** Try making the enemy smarter! Ideas:
- Move randomly sometimes
- Choose diagonal moves
- Patrol in a pattern
- Use different strategies for different enemies

### 7. Add WASD Controls

In `game.py`, find `handle_input()` and add this:

```python
elif event.type == pygame.KEYDOWN:
    # Existing arrow key code...
    
    # NEW: Add WASD controls
    if event.key == pygame.K_w:
        self.player.set_direction(0, -1)
    elif event.key == pygame.K_s:
        self.player.set_direction(0, 1)
    elif event.key == pygame.K_a:
        self.player.set_direction(-1, 0)
    elif event.key == pygame.K_d:
        self.player.set_direction(1, 0)
```

### 8. Customize the Game Over Screen

In `renderer.py`, find `draw_game_over_screen()`:

```python
if won:
    title_text = self.font_large.render(
        "YOU WIN!",  # Change this text!
        True,
        (0, 255, 0)  # Change this color!
    )
```

---

## 🐛 Learning Points & Bug Challenges

This code contains **intentional learning opportunities**. Can you find them?

### Bug #1: Position Validation (Beginner)

**Location:** `entities.py`, in the `Player._is_valid_position()` method

**Hint:** What happens when the player goes to the very edge of the map?

**Challenge:** Find and fix the bug. What causes the player to get stuck?

---

### Bug #2: Incomplete Restart (Beginner)

**Location:** `game.py`, in the `handle_input()` method

**Hint:** The comment says "Try typing 'R' to restart" but it won't work!

**Challenge:** Find why pressing R doesn't work, and fix it.

**Bonus:** What's the alternative way to restart shown in the game over screen?

---

### Learning Challenge #3: Coin Placement (Intermediate)

**Location:** `game.py`, in the `_generate_coins()` method

**Current behavior:** Coins are placed in EVERY empty space (there are ~200 coins!)

**Challenge:** Modify the coin generation to:
1. Use `import random` at the top of the file
2. Place coins in only 50 random empty spaces
3. Hint: Use `random.sample()` or `random.choice()`

---

### Learning Challenge #4: Smart Enemy AI (Intermediate to Advanced)

**Location:** `entities.py`, in the `Enemy.update_position()` method

**Current behavior:** Enemies move directly toward the player (they're dumb!)

**Challenge:** Try one of these:
1. Make enemies move randomly sometimes
2. Implement different behaviors for each enemy
3. Make enemies patrol a specific path
4. Add a "personality" to each enemy

---

### Learning Challenge #5: Add More Game Features (Advanced)

Try adding these features:

**Easy:**
- Add a third enemy
- Add a power-up that makes the player faster
- Add a sound effect when collecting coins (use pygame.mixer)

**Medium:**
- Add a timer/score system
- Make enemies spawn from a "base" location
- Add difficulty levels that increase over time

**Hard:**
- Add a level system (complete one maze, move to the next)
- Implement a high score system using files
- Add special enemies with unique behaviors
- Create a menu screen

---

## 🔧 Troubleshooting

### Problem: "Module 'pygame' not found"

**Solution:** Install pygame:
```bash
pip install pygame
```

### Problem: Game runs but nothing appears on screen

**Solution:** Try these steps:
1. Make sure all files are in the same folder
2. Check that `config.py` is in the same folder as `main.py`
3. Try running in a different terminal/command prompt

### Problem: "SyntaxError" or "IndentationError"

**Solution:** 
1. Check that you didn't accidentally break the code while editing
2. Make sure lines are properly indented (spaces at the start)
3. Look at the line number VS Code shows you

### Problem: Colors look different than expected

**Solution:** 
1. RGB values go from 0-255, not 0-100
2. Try using an RGB picker online: https://www.colorpicker.com/
3. Remember the format: `(Red, Green, Blue)`

### Problem: Player/Enemy stuck in walls

**Solution:** 
This might be Bug #1! Check the `_is_valid_position()` method in `entities.py`.

---

## 📚 File Structure Summary

```
your-maze-game/
├── main.py              ← Run this file!
├── config.py            ← Customize colors, speeds, maze
├── entities.py          ← Player, Enemy, Coin classes
├── game.py              ← Game logic
├── renderer.py          ← Drawing and UI
└── requirements.txt     ← Python packages to install
```

---

## 💡 Tips for Success

1. **Start small:** Make small changes and test them
2. **Read the code:** Every file has comments explaining what each part does
3. **Don't be afraid to break it:** That's how you learn!
4. **Use print():** Add `print()` statements to debug
5. **Test frequently:** After each change, run the game

---

## 🎯 Next Steps

1. ✅ Get the game running
2. ✅ Change some colors to make it your own
3. ✅ Try to find Bug #1 or Bug #2
4. ✅ Design your own maze
5. ✅ Add WASD controls
6. ✅ Improve the enemy AI
7. ✅ Add a new feature

---

**Happy coding! 🚀**

Have fun customizing your game and learning Python!
