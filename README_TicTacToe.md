Tic-Tac-Toe Game
Project Description

This is a simple two-player Tic-Tac-Toe game developed using Python. 
The game runs in the console and does not require any external libraries or a database.

Player 1 uses X and Player 2 uses O. Players take turns choosing an empty position on a 3 × 3 board.

The first player to get three matching symbols in a row, column, or diagonal wins.

Features
3 × 3 game board
Two-player gameplay
Player 1 uses X
Player 2 uses O
Players take turns on the same keyboard
Position selection from 1 to 9
Input validation
Handles non-numeric input
Handles out-of-range input
Prevents selecting an occupied cell
Handles empty input
Win detection
Draw detection
Play-again option
Score tally across multiple rounds
Friendly error messages
Exception handling


The program demonstrates:

Variables and data types
Functions
Lists
Loops
Conditional statements
String formatting
User input
Basic exception handling

No external libraries or database are required.

How to Run
Step 1

Install Python on your computer.

Step 2

Open the project in PyCharm.

Step 3

Open the Python file containing the Tic-Tac-Toe program.

For example:

tic_tac_toe.py
Step 4

Click the Run button in PyCharm.

The game will start in the console.

How to Play

The board contains positions from 1 to 9:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player 1 enters a position to place X.

Player 2 enters a position to place O.

Players continue taking turns until:

Player 1 wins
Player 2 wins
The board is full and the game is a draw
Input Validation

The program checks for invalid input.

It prevents:

Empty input
Non-numeric input
Numbers outside 1–9
Selecting an already occupied position

When invalid input is entered, a friendly error message is displayed and the same player gets another chance.

Win Detection

A player wins by getting three of their symbols in:

Any row
Any column
Either diagonal

Example:

 X | O | X
---+---+---
 O | X | O
---+---+---
   |   | X

Player 1 wins because X appears diagonally.

Draw Detection

If all nine positions are occupied and neither player has won, the game ends in a draw.

The program displays:

It's a draw! The board is full.
Score Tally

The game keeps track of the results across multiple rounds.

The score includes:

Player 1 (X): 2
Player 2 (O): 1
Draws: 1

The scores continue to update when players choose to play another round.

Play Again

After each round, the program asks:

Do you want to play another round? (y/n):

Enter:

y or Y to start another round
n or N to stop

When the players finish, the program displays a friendly closing message.

Project Structure
Tic-Tac-Toe/
│
├── tic_tac_toe.py
└── README.md
tic_tac_toe.py

Contains the complete Python source code for the game.

README.md

Contains information about the project and instructions for running and playing the game.

Conclusion

This project demonstrates basic Python programming concepts including functions, 
lists, loops, conditional statements, string formatting, input validation, exception handling, 
win detection, draw detection, and maintaining a score across multiple rounds.