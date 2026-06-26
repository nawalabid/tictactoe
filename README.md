# Tic Tac Toe Game 

A simple and interactive **Tic Tac Toe** game built using **Python** and **Tkinter**. 
This project features a graphical user interface (GUI), player selection, a live scoreboard, and to play multiple rounds.

---

##  Features

*  Classic 2-player Tic Tac Toe gameplay
*  Random or user-selected starting player
*  Automatic win and draw detection
*  Scoreboard
    (Player X wins. Player O wins, Draw count)
*  Play Again option
*  Quit Game button
*  Centered, fixed-size GUI window
*  Popup messages for game results

---

## Technologies Used

* Python 3.12
* Tkinter (GUI Library)
* Random Module
* Functools (`partial`)

---

## How to Play

1. Select the starting player:
   * Random
   * Player X
   * Player O
2. Click **"CLICK HERE TO START"**.
3. Players take turns placing **X** and **O** on the board.
4. The first player to align three symbols horizontally, vertically, or diagonally wins.
5. If all squares are filled without a winner, the game ends in a draw.
6. Choose:
   * **Play Again** to start another round.
   * **Quit Game** to exit.

---

## Winning Conditions

A player wins by placing three identical symbols in:

* A horizontal row
* A vertical column
* A diagonal

If all nine cells are filled without a winner, the match is declared a draw.

---

## Scoreboard

The scoreboard automatically updates after every game and keeps track of:

* Player X Wins
* Player O Wins
* Draws


