# ============================================================================
# MAZE GAME - MAIN
# ============================================================================
# Run this file to start the game!
# python main.py
# 
# CUSTOMIZATION TIPS:
# 1. Open config.py to change colors, speeds, and maze layout
# 2. Open entities.py to improve the enemy AI
# 3. Open renderer.py to change the game over screen
# 4. Add your own features and bugs to fix!
# ============================================================================

from game import Game

if __name__ == "__main__":
    # Create a new game instance
    game = Game()
    
    # Run the game (this will block until the window is closed)
    game.run()
