# Solving Sudoku With Classical AI Problem Solving Techniques


## Abstract

This is a fun project I did in the AI class in college, where there was the classical AI topics brought to understand the foundamentals of AI from the classical perspective.
The code solves Sudoku in 3 ways, each way is better than the one before, and you will notice how the time geting reduced linearly.


## Introduction

In the realm of Artificial Intelligence, Constraint Satisfaction Problems (CSPs) have been a topic
of significant interest due to their wide range of applications. One such application is the popular
logic-based number placement puzzle, Sudoku. The objective of this project is to represent Sudoku
as a CSP and devise solutions using three different algorithms: Standard Backtracking (BT),
Forward Checking (FC), and Maintaining Arc-Consistency (MAC).

The project will commence with the formulation of the Sudoku puzzle as a CSP, defining the
variables, their respective domains, and the constraints that govern them. Following this, we will
implement three Python functions that embody the BT, FC, and MAC algorithms.

To evaluate the effectiveness of these algorithms, we will test them on a dataset of 20 Sudoku
puzzles. The performance of each algorithm will be assessed based on the time taken to solve each
puzzle.

Finally, we will analyze and comment on our results by highlighting the best, worst, and average
time taken by each function to solve the puzzles. This analysis will be visually represented in a
comprehensive figure summarizing all results. Through this project, we aim to gain insights into
the efficiency and effectiveness of these algorithms in solving Sudoku puzzles as CSPs.

## Understanding Sudoku and Constraint Satisfaction Problems (CSPs)

Sudoku is a logic-based number placement puzzle that has gained worldwide popularity. The
objective of the game is to fill a 9 × 9 grid with digits so that each column, each row, and each of
the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9. The puzzle setter
provides a partially completed grid, which typically has a unique solution.

A Constraint Satisfaction Problem (CSP) is a mathematical problem defined as a set of objects
whose state must satisfy a number of constraints or restrictions. CSPs represent the entities in a
problem as a homogeneous collection of finite constraints over variables, which is solved by
constraint satisfaction methods. CSPs are a powerful concept for expressing and solving problems
in various areas, such as artificial intelligence, computer science, and operations research.

Formulating Sudoku as a CSP involves the following steps:
1. Variables: Each cell in the Sudoku grid is considered as a variable. This gives us 81 variables
(9 𝑟𝑜𝑤𝑠 × 9 𝑐𝑜𝑙𝑢𝑚𝑛𝑠), each with a domain of {1,2, … ,9}.
2. Domains: The domain of each variable (cell) is the set of numbers from 1 to 9.
3. Constraints: The constraints are based on the rules of Sudoku:
   - All numbers in each row must be different.
   - All numbers in each column must be different.
   - All numbers in each 3 × 3 grid must be different.
   - If the Sudoku puzzle is partially completed, there are additional constraints for each
cell that contains a number.

By formulating Sudoku as a CSP, we can apply various algorithms used for solving CSPs to solve
Sudoku puzzles.

## Algorithms Design and Implementation

In this section we will discuss the implementation, and the code of these algorithms will be later
seen attached as an appendix.

### 1. Backtracking

To implement the backtracking, we only needed to have to functions to solve the sudoku puzzle:

- `backtracking`:
The function that performs the search on the state space to find the solution, and it takes the
following parameters:
  - The sudoku puzzle/Problem/CSP: in which is the CSP in what the book states in the
backtracking algorithm's pseudocode and depends on the level of iteration and the cell
in which it performs the algorithm on.
  - Row and column: in which it can indicate the cell and to impose the constraints for
which it won't contradict with other values based on the constraints.

- `is_valid_move`:
The function that checks for the value in cell for which it violates the constraints or not, and it
takes the parameter:
  - Number: In addition to the state space and successor function, this function checks if
the number meets the constraints in which it doesn't conflict with other numbers.

### 2. Forward-checking

The main thing which differentiates the forward-checking from the backtracking in our
implementation is that we added a parameter which is called domain, and all it does is storing the
values in which it was assigned to preserve its place and accelerates the searching process.

All what we understand about the forward-checking technique is that it accelerates the searching
process by defining a forward assignment of values to increase the speed of the searching process.

### 3. Maintaining Arc-Consistency

The revise function checks each possible number (from 1 to 9) for the current cell. If
`is_valid_move` returns False for a number (i.e., placing that number in the current cell would
violate the Sudoku rules), it sets revised to True.

The `ac3` function maintains arc consistency. It creates a queue of all arcs (pairs of cells that are in
the same row or column or block). For each arc in the queue:
- It removes the arc from the queue and makes it arc-consistent by calling `revise`.
- If `revise` returns True (i.e., it had to remove a number from the domain of a variable), it adds
all other arcs that involve that variable back into the queue.

The `mac` function is similar to your original backtracking function. However:
- Before it assigns a number to a cell and recursively calls itself to fill in the rest of the grid
(`mac(grid)`), it first checks whether the assignment maintains arc consistency by calling
`ac3(grid)`.
- If `ac3(grid)` returns False, it means that the current assignment does not maintain arc
consistency (i.e., there's no valid number that can be placed in some cell), so it undoes the
assignment (`grid[row][col] = 0`) and continues with the next number.
- If all numbers have been tried and none of them leads to a valid solution (i.e., `mac(grid)`
always returns False), then it returns False to backtrack to the previous cell.

## Results Discussion

We ran 20 sudoku puzzles on the three algorithms, for which it gave us the time taken to
analyze these algorithms, and the findings was as seen on the table above, the linear decrease in time
from backtracking to the mac algorithm which accelerated the solving of the algorithm, and
ensured the imposing of a maintained arc-consistency.

## Conclusion

We described the Sudoku as a CSP, and represented the domains, variables, and constraints for it,
and then we implemented the algorithms for backtracking, forward-checking, and maintaining
arc-consistency, and after analyzing the results of executing 20 puzzles, we conclude that the
mac algorithm has the least execution time taken to solve the sudoku.

## Contributions
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.


**Shoutout to my colleague Yousef Hamad Al-Khuraiji for contributing in this project**
