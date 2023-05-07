# Sudoku_Solver

The following code is a simple Sudoku game solver written in Python. Based on the rules of the game, the small program applies brute force and backtracking to solve the game.

## About Sudoku

The popular Japanese puzzle game Sudoku is based on the logical placement of numbers. An online game of logic, Sudoku doesn’t require any calculation nor special math skills; all that is needed are brains and concentration.

## How to play Sudoku

The goal of Sudoku is to fill in a $9×9$ grid with digits so that each column, row, and $3×3$ section contain the numbers between $1$ to $9$. At the beginning of the game, the $9×9$ grid will have some of the squares filled in. Your job is to use logic to fill in the missing digits and complete the grid. Don’t forget, a move is incorrect if:

* Any row contains more than one of the same number from $1$ to $9$
* Any column contains more than one of the same number from $1$ to $9$
* Any 3×3 grid contains more than one of the same number from $1$ to $9$

## Sudoku Tips

Sudoku is a fun puzzle game once you get the hang of it. At the same time, learning to play Sudoku can be a bit intimidating for beginners. So, if you are a complete beginner, here are a few Sudoku tips that you can use to improve your Sudoku skills.

* Tip 1: Look for rows, columns of $3×3$ sections that contain $5$ or more numbers. Work through the remaining empty cells, trying the numbers that have not been used. In many cases, you will find numbers that can only be placed in one position considering the other numbers that are already in its row, column, and $3×3$ grid.

* Tip 2: Break the grid up visually into $3$ columns and $3$ rows. Each large column will have $3$, $3×3$ grids and each row will have $3$, $3×3$ grids. Now, look for columns or grids that have $2$ of the same number. Logically, there must be a 3rd copy of the same number in the only remaining 9-cell section. Look at each of the remaining $9$ positions and see if you can find the location of the missing number.

Now that you know a little more about Sudoku, play and enjoy this game.



This will open a window that allows you to input a Sudoku board. To input a number, click on the corresponding box and type in the number. The program will automatically check if the number is valid or not. Once all the numbers have been inputted, click the "Solve" button to solve the board.

## Credits

This program was developed by Ruddy. If you have any questions or comments, feel free to contact me.
