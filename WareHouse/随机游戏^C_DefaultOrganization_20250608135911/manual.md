```markdown
# Guess the Number Game

Welcome to the "Guess the Number" game! This is a simple yet engaging game where players try to guess a randomly generated number between 1 and 100. 

## Main Functions

- **Random Number Generation**: The game generates a random number that the player must guess.
- **User Input**: Players can input their guesses through a graphical user interface (GUI).
- **Feedback Mechanism**: The game provides feedback on whether the guess is too low, too high, or correct.
- **Attempt Tracking**: The game keeps track of the number of attempts taken to guess the correct number.
- **Game Reset**: Players can reset the game to start a new round.

## Installation Instructions

To run the "Guess the Number" game, you need to install the required dependencies. Follow these steps:

1. **Install Python**: Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv guess_the_number_env
   source guess_the_number_env/bin/activate  # On Windows use `guess_the_number_env\Scripts\activate`
   ```

3. **Install Dependencies**: Use the following command to install the required dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:
   ```
   pygame>=2.0.1,<3.0.0
   ```

## How to Play

1. **Run the Game**: After installing the dependencies, navigate to the directory containing the game files and run the main script:
   ```bash
   python main.py
   ```

2. **Game Interface**: A window will appear with an input box and a message area. 

3. **Make a Guess**: Click on the input box and type your guess (a number between 1 and 100). Press `Enter` to submit your guess.

4. **Receive Feedback**: The game will inform you if your guess is too low, too high, or correct. If you guess correctly, it will display the number of attempts you took.

5. **Reset the Game**: To start a new game, simply enter a guess after the game ends, and it will reset automatically.

## Enjoy the Game!

Have fun playing "Guess the Number"! Challenge your friends and see who can guess the number in the fewest attempts!
```