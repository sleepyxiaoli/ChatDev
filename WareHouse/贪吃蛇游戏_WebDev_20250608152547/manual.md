```markdown
# Classic Snake Game

A simple implementation of the classic Snake game using Python and Pygame. This game includes a scoring system and collision detection for game over conditions.

## Main Functions

- **Snake Movement**: Control the snake using the arrow keys.
- **Food Consumption**: Eat food to grow the snake and increase your score.
- **Collision Detection**: The game ends if the snake collides with the walls or itself.
- **Score Display**: The current score is displayed on the screen.

## Quick Install

To run the Snake game, you need to install the required dependencies. You can do this using pip:

```bash
pip install -r requirements.txt
```

Alternatively, if you prefer to use conda, you can install Pygame from conda-forge:

```bash
conda install -c conda-forge pygame
```

## 🤔 What is this?

The Classic Snake Game is a fun and engaging way to test your reflexes and strategic thinking. The objective is to control the snake to eat food while avoiding collisions with the walls and itself. The game keeps track of your score, which increases each time you consume food.

## 🎮 How to Play

1. **Run the Game**: Execute the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Control the Snake**:
   - Use the **UP** arrow key to move the snake up.
   - Use the **DOWN** arrow key to move the snake down.
   - Use the **LEFT** arrow key to move the snake left.
   - Use the **RIGHT** arrow key to move the snake right.

3. **Objective**: Eat the red food squares to grow the snake and increase your score. 

4. **Game Over**: The game ends if the snake collides with the walls or itself. 

5. **Score Display**: Your current score is displayed in the top left corner of the screen.

## 📖 Documentation

For more detailed information about the code structure and functionality, refer to the following files:

- **main.py**: The entry point for the game.
- **snake.py**: Contains the logic for the Snake class, including movement and collision detection.
- **food.py**: Manages the food generation within the game.
- **game.py**: Contains the Game class that orchestrates the game logic and rendering.

Feel free to modify the code to enhance the game or add new features!
```