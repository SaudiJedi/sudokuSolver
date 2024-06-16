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

## Testing Results And Analysis

<br>
<br>

<table class="TableGrid" border="0" cellspacing="0" cellpadding="0" width="623" style="width:467.45pt;margin-left:.3pt;border-collapse:collapse;mso-yfti-tbllook:
 1184;mso-padding-alt:.7pt 5.35pt 0in 5.35pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-right:none;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:26.9pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 1 </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border:solid black 1.0pt;
  border-left:none;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.4pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.35pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 7 4 0 2 0 0 8 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 0 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">9 0 0 0 8 0 7 1 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 7 3 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 0 0 8 0 5<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.1pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">4 0 8 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 0 9 4 0 8<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 5 0 3 0 0 0 2 0 </p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">1 2 3 8 5 4 6 9 7<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:36.6pt;text-align:left;text-indent:-9.0pt;
  line-height:107%;mso-list:l7 level1 lfo5"><!--[if !supportLists]--><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span><!--[endif]--><span dir="LTR"></span>7 4 9 2 6 3 8 1<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:36.6pt;text-align:left;text-indent:-9.0pt;
  line-height:107%;mso-list:l7 level1 lfo5"><!--[if !supportLists]--><span style="mso-list:Ignore">6<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span><!--[endif]--><span dir="LTR"></span>8 9 1 3 7 2 5 4<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">9 4 2 6 8 5 7 1 3<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">8 1 5 4 7 3 9 6 2<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:36.6pt;text-align:left;text-indent:-9.0pt;
  line-height:107%;mso-list:l2 level1 lfo6"><!--[if !supportLists]--><span style="mso-list:Ignore">3<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span><!--[endif]--><span dir="LTR"></span>6 7 2 9 1 8 4 5<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.1pt;margin-left:36.6pt;text-align:left;text-indent:-9.0pt;
  line-height:107%;mso-list:l2 level1 lfo6"><!--[if !supportLists]--><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span><!--[endif]--><span dir="LTR"></span>9 8 7 1 2 5 3 6<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">2 3 1 5 6 9 4 7 8<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">7 5 6 3 4 8 1 2 9 </p>
  </td>
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:20.6pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">1076.882 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.35pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Forward-</p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Checking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:18.55pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.0449 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:2.9pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:42.95pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:42.95pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.023 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:26.9pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 2 </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.4pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">3 0 5 7 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 8 0 0 0 7 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 9 0 4 8 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 1 0 0 0 0 9 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 3 0 0 0 4 8 6 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 1 6 5 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 7 4 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.1pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 3 0 0 0 0 0 9<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 0 0 0 0 0 </p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">3 2 5 7 6 1 4 9 8<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">1 4 8 2 3 9 7 5 6<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">6 7 9 5 4 8 1 2 3<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">5 1 6 8 2 7 9 3 4<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:36.6pt;text-align:left;text-indent:-9.0pt;
  line-height:107%;mso-list:l24 level1 lfo7"><!--[if !supportLists]--><span style="mso-list:Ignore">7<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span><!--[endif]--><span dir="LTR"></span>3 2 9 5 4 8 6 1<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:36.6pt;text-align:left;text-indent:-9.0pt;
  line-height:107%;mso-list:l24 level1 lfo7"><!--[if !supportLists]--><span style="mso-list:Ignore">8<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span><!--[endif]--><span dir="LTR"></span>9 4 3 1 6 5 7 2<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">2 8 7 4 9 3 6 1 5<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.1pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">4 6 3 1 7 5 2 8 9<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">9 5 1 6 8 2 3 4 7 </p>
  </td>
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:20.6pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">4.278 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.35pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Forward-</p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Checking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:18.55pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.0776 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:2.9pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:42.9pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:42.9pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.01489 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:26.9pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 3 </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.4pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 0 3 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 5 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">6 0 0 0 0 4 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">3 0 4 0 2 0 0 7 1<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 6 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 2 8 0 0 7 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 4 5 0 8 2 3 0 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">2 0 0 0 0 0 0 9 0<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:29.65pt;text-align:left;text-indent:0in;
  line-height:107%">0 0 0 5 0 0 0 0 0 </p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">1 7 2 6 3 5 4 8 9<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">4 5 3 1 9 8 2 6 7<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">6 8 9 2 7 4 1 5 3<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">3 9 4 8 2 6 5 7 1<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">7 1 6 4 5 3 9 2 8<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">5 2 8 9 1 7 6 3 4<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">9 4 5 7 8 2 3 1 6<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">2 6 7 3 4 1 8 9 5<span style="mso-spacerun:yes">&nbsp; </span></p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:27.6pt;text-align:left;text-indent:0in;
  line-height:107%">8 3 1 5 6 9 7 4 2 </p>
  </td>
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:20.6pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">1.37 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.35pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Forward-</p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Checking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:18.65pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.0466 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:2.9pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:42.85pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:42.85pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.05pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.00939 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:26.9pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 4 </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.4pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="132" valign="top" style="width:99.05pt;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;mso-border-right-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 6 1 0 8 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 5 0 0 4 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 9 0 0 7 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 9 0 4 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 4 2 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 1 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 0 5 0 0 3 6 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 6 9 0 0 0 7 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 1 0 6 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 3 7 4 6 1 5 8 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 6 8 2 5 9 3 4 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l20 level1 lfo8"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 9 3 8 7 1 2 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l20 level1 lfo8"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 3 7 9 8 4 6 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l20 level1 lfo8"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">6<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 1 5 3 4 2 9 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l3 level1 lfo9"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">8<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 4 6 1 2 7 3 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l3 level1 lfo9"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">9<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 5 8 7 3 6 1 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 6 9 2 5 8 7 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin:0in;text-align:center;
  text-indent:0in;line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:
  12.0pt;line-height:107%">7 8 2 1 4 6 9 5 3 </span></p>
  </td>
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:20.6pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">6.2022 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.35pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Forward-</p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Checking </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:18.55pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.05789 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;height:14.2pt">
  <td width="132" rowspan="2" valign="top" style="width:99.05pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.3pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 5.35pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:2.9pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:31;mso-yfti-lastrow:yes;height:32.5pt">
  <td width="102" valign="top" style="width:76.2pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 5.35pt 0in 5.35pt;height:32.5pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%">0.009 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
<tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.2pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-right:none;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 5 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border:solid black 1.0pt;
  border-left:none;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.3pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 3 8 4 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 5 0 0 6 0 9 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 7 0 0 0 0 4 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 6 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 1 8 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 8 2 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 0 0 0 0 6 0 0 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 2 0 0 0 4 6 0 9 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 6 3 8 4 9 2 5 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 5 2 3 6 7 9 1 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 9 7 2 5 1 3 4 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l1 level1 lfo10"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">2<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 6 4 7 5 8 9 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l1 level1 lfo10"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">3<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 4 9 1 8 5 6 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 8 5 6 2 3 1 7 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l0 level1 lfo11"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">6<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 9 5 8 2 7 3 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l0 level1 lfo11"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">7<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 8 1 9 6 4 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.65pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 2 1 7 3 4 6 8 9 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:20.5pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.5pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2744.953 <span class="SpellE">ms</span> </span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:18.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.04389 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:32.45pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:32.45pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0087 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 6 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 5 0 0 1 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 3 7 6 0 0 1 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 9 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 9 4 0 0 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 1 2 0 0 0 7 6 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 1 0 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 0 0 0 6 7 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 4 5 3 7 1 6 8 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 3 7 6 5 9 1 4 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 6 9 2 8 4 5 7 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l16 level1 lfo12"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">3<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 6 9 4 5 8 1 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l16 level1 lfo12"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 8 7 1 2 3 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 9 1 8 3 6 4 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l14 level1 lfo13"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 2 4 9 3 7 6 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l14 level1 lfo13"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">6<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 3 1 2 8 9 5 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.65pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 8 4 5 6 7 2 3 1 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:20.5pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.5pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1.0711 <span class="SpellE">ms</span> </span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:18.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0.0759 <span class="SpellE">ms</span> </span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:14.25pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:32.5pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:32.5pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.008 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 7 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 0 0 0 0 4 9 0 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 0 9 0 0 5 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 3 2 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 0 0 0 0 0 4 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 3 6 0 8 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 5 0 0 1 0 6 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 8 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 1 2 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 1 2 8 7 4 9 3 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 4 9 2 6 5 1 7 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 6 8 1 9 3 2 4 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 2 3 7 5 8 4 1 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 7 4 9 3 6 5 8 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 9 5 4 2 1 3 6 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 3 1 6 8 9 7 5 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 8 7 5 1 2 6 9 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.65pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 5 6 3 4 7 8 2 1 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.961 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:18.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0453 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:32.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:32.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.01 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
<tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.25pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-right:none;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 8 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border:solid black 1.0pt;
  border-left:none;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 0 7 0 9 4 0 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 7 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 4 0 5 0 1 0 0 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 6 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 3 6 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 8 0 3 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 6 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 9 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 1 7 6 9 4 3 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 5 9 8 7 3 1 4 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 4 3 5 2 1 7 9 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 2 6 4 5 9 8 7 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 3 5 1 8 7 9 6 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 7 8 3 6 2 5 1 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 9 1 2 4 8 6 3 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 6 2 9 3 5 4 8 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 8 4 7 1 6 2 5 9 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">1.492 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0366 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0082 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 9 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:14.25pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 8 2 0 5 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 1 6 0 0 4 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 0 0 0 1 0 0 0 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 9 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 5 9 4 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 0 0 0 5 0 3 6 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 1 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 4 9 1 8 2 7 5 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 2 7 4 9 5 6 1 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 8 1 6 3 7 4 9 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 9 2 7 1 3 5 8 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 3 8 5 2 6 9 7 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 6 5 9 4 8 2 3 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 7 4 8 5 1 3 6 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 1 6 3 7 4 8 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 5 3 2 6 9 1 4 7 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">2.2245 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0461 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes, </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0085 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 10 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 5 0 6 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 7 4 0 0 9 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 8 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 0 0 0 0 0 4 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 4 1 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 0 4 0 0 9 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 7 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 5 0 0 2 8 0 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 8 0 0 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 2 3 9 5 8 6 7 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 8 7 4 1 6 9 2 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 9 6 2 3 7 5 8 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 9 6 7 5 2 4 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l12 level1 lfo14"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">7<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 2 3 8 4 1 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l12 level1 lfo14"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">8<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 4 1 2 9 3 5 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l12 level1 lfo14"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">9<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 8 5 6 1 7 3 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 3 5 7 4 2 8 1 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 7 1 8 9 3 4 6 5 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">3.9472 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:14.25pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:18.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0448 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes, </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0123 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 11 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 0 0 0 7 0 9 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 0 0 0 8 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 4 2 0 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 6 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 8 5 6 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 0 0 0 3 0 0 0 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 4 7 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 3 9 0 0 4 2 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 2 6 7 5 9 4 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 4 7 1 8 9 2 3 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 5 9 3 4 2 1 6 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 6 5 2 9 3 8 1 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 2 1 8 5 6 3 7 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 3 8 4 1 7 6 5 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 8 4 7 3 1 5 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 9 6 5 2 4 7 8 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 7 3 9 6 8 4 2 1 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">227.3165 <span class="SpellE">ms</span> </span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.045 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:31;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0086 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
<tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.25pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-right:none;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 12 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border:solid black 1.0pt;
  border-left:none;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 4 1 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 0 2 0 0 9 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l19 level1 lfo15"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">0<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 7 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l19 level1 lfo15"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">1<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 0 5 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 1 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 7 0 0 0 0 0 4 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 8 0 0 0 6 0 7 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 4 0 3 7 1 0 0 5 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 4 7 2 5 6 8 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l11 level1 lfo16"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">7<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 9 6 8 3 4 1 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l11 level1 lfo16"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">8<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 2 4 1 9 3 5 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 2 7 8 3 4 5 9 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 3 8 5 9 2 7 6 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 9 5 1 6 7 2 3 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 7 3 9 5 8 1 4 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 8 1 2 4 6 9 7 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 4 6 3 7 1 8 2 5 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">2004.98 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0453 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes, </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0237 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 13 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:14.25pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 1 5 9 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 1 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 5 0 0 0 0 0 0 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 3 0 7 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 2 5 0 0 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 7 0 0 0 3 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 2 0 0 3 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 9 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 4 5 0 2 0 3 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 4 3 8 1 5 9 7 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 7 8 4 2 9 5 1 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 5 1 3 6 7 2 4 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 3 2 7 8 6 4 5 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l5 level1 lfo17"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 6 2 5 3 1 8 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l5 level1 lfo17"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 7 9 4 1 3 6 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 2 5 1 3 8 6 9 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 9 6 7 4 8 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 6 4 5 9 2 7 3 1 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">2.09 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0748 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes, </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.008 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 14 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 0 0 0 0 0 0 9 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 4 0 0 0 9 0 0 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 7 0 0 0 0 4 8 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 3 0 9 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 0 0 6 0 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 8 0 0 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 0 0 9 2 0 1 0 5 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 1 5 2 4 8 7 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 4 8 7 6 9 5 1 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 7 9 1 3 5 4 8 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 6 3 5 9 7 8 2 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 8 2 6 1 3 9 5 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 9 1 4 8 2 3 6 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 2 7 8 5 4 6 3 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 5 6 3 7 1 2 4 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 3 4 9 2 6 1 7 5 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">2.0139 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:14.25pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:18.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:18.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0442 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0177 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 15 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 3 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 9 1 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 7 0 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 0 0 0 0 3 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 7 1 9 6 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 9 6 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l17 level1 lfo18"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">0<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 7 0 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l17 level1 lfo18"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">1<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 9 0 0 5 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 2 3 1 5 8 6 7 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 9 1 2 6 4 3 5 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 5 8 7 3 9 1 2 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l18 level1 lfo19"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">2<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 6 9 4 3 5 8 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:1.0pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l18 level1 lfo19"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">3<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 4 5 7 1 9 6 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 7 5 6 8 2 4 3 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 3 7 4 9 6 2 1 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 4 2 3 1 7 8 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 6 9 8 2 5 7 4 3 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">4.3833 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.053 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt .2pt 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:31;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt .2pt 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes, </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.009 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
<tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.25pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-right:none;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 16 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border-top:solid black 1.0pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border:solid black 1.0pt;
  border-left:none;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 4 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 7 0 0 0 2 6 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 0 6 1 0 4 0 0 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 9 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 0 0 0 1 7 2 6 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 7 0 0 0 8 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 0 0 0 0 9 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l4 level1 lfo20"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 3 6 7 8 5 9 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l4 level1 lfo20"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 8 9 4 1 3 7 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 7 9 3 5 2 6 4 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 8 6 1 9 4 7 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 1 2 5 8 6 9 3 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 5 4 7 2 3 1 8 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 9 5 4 1 7 2 6 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 4 7 2 3 5 8 1 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.65pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 3 1 8 6 9 4 5 7 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">37.62 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.06 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:32.45pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:32.45pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0232 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 17 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:14.3pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 9 0 0 2 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 7 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 2 0 0 0 7 0 9 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 9 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 8 0 0 7 0 0 0 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 3 0 0 0 0 0 1 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 0 9 0 1 0 0 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 2 0 0 4 9 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 9 3 4 2 5 6 7 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 4 7 3 6 9 1 2 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 2 5 1 8 7 4 9 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l9 level1 lfo21"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">2<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 4 6 3 1 7 8 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l9 level1 lfo21"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">3<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 6 9 4 8 2 5 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 8 1 5 7 2 3 6 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l13 level1 lfo22"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 8 7 9 6 5 1 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:7.55pt;text-align:center;text-indent:-7.55pt;
  line-height:107%;mso-list:l13 level1 lfo22"><!--[if !supportLists]--><span style="font-size:10.0pt;line-height:107%"><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 9 2 1 3 8 4 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 1 2 8 5 4 9 3 6 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:20.5pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.5pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">7.9486 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:18.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.1227 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:28.15pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:28.15pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.018 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 18 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:14.3pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 4 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 9 0 7 6 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 0 0 0 0 5 0 0 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 2 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 4 9 2 0 0 0 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 7 0 8 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 2 0 5 4 0 1 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l6 level1 lfo23"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">1<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 6 7 8 2 4 5 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l6 level1 lfo23"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">2<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 5 1 9 3 7 6 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 9 8 5 4 6 1 3 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 2 1 4 7 5 8 9 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 5 7 6 3 8 2 4 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l8 level1 lfo24"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">3<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 4 9 2 1 6 7 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l8 level1 lfo24"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">4<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 3 8 6 9 5 2 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:8.3pt;text-align:center;text-indent:-8.3pt;
  line-height:107%;mso-list:l8 level1 lfo24"><!--[if !supportLists]--><span style="font-size:11.0pt;line-height:107%"><span style="mso-list:Ignore">5<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span dir="LTR"></span><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 9 2 1 7 3 8 4<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.65pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 7 2 3 5 4 9 1 6 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:20.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">2190.23 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:14.3pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:18.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.048 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:32.45pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:32.45pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes, </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0085 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 19 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:14.35pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.35pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 7 0 0 0 0 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 8 0 0 5 0 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 0 0 4 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 5 0 1 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 9 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 6 5 0 0 3 0 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 7 0 6 0 0 9 0 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.8pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 7 0 0 0 4 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 2 4 7 5 9 6 8 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 3 7 8 1 2 5 4 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 9 8 4 3 6 1 7 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 5 3 1 8 4 7 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 6 1 2 9 7 8 3 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 8 9 3 6 5 4 2 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:1.0pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 4 6 5 2 8 3 1 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:.9pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 7 2 6 4 1 9 5 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.65pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:11.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 1 5 9 7 3 2 6 4 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">7.7294 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:18.55pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.55pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.04 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:31;height:32.5pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:32.5pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:1.0pt;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Yes </p>
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0086 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:33;height:14.25pt">
  <td width="198" valign="top" style="width:148.2pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-left-alt:solid black .5pt;mso-border-bottom-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border:none;border-bottom:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-top-alt:solid black .5pt;
  mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.25pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:24.25pt;text-align:center;text-indent:0in;
  line-height:107%">Sudoku 20 </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-top-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.25pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:34;height:14.3pt">
  <td width="198" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku before solving </p>
  </td>
  <td width="192" valign="top" style="width:2.0in;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.9pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Sudoku after solving </p>
  </td>
  <td width="139" valign="top" style="width:104.15pt;border:none;border-bottom:
  solid black 1.0pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-left-alt:
  solid black .5pt;mso-border-bottom-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin:0in;text-align:left;text-indent:
  0in;line-height:107%"><span style="mso-spacerun:yes">&nbsp;</span></p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-top-alt:solid black .5pt;mso-border-bottom-alt:
  solid black .5pt;mso-border-right-alt:solid black .5pt;background:#E7E6E6;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.3pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:8.0pt;margin-left:0in;text-align:left;text-indent:0in;
  line-height:107%"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:35;height:14.2pt">
  <td width="198" rowspan="6" valign="top" style="width:148.2pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 5 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 1 9 0 0 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 3 5 7 0 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 9 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 6 0 7 2 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 2 0 0 8 3 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 0 0 0 0 4 0 0 0<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">0 3 0 0 0 7 0 0 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 5 0 0 0 1 0 0 0 </span></p>
  </td>
  <td width="192" rowspan="6" valign="top" style="width:2.0in;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">2 7 5 1 9 6 3 4 8<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">6 1 9 3 4 8 2 5 7<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">8 4 3 5 7 2 1 9 6<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">5 6 7 2 1 9 4 8 3<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.85pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">3 8 1 4 6 5 7 2 9<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">9 2 4 7 8 3 6 1 5<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">1 9 6 8 3 4 5 7 2<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.1pt;
  margin-bottom:.95pt;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">4 3 2 9 5 7 8 6 1<span style="mso-spacerun:yes">&nbsp; </span></span></p>
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.85pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%"><span style="font-size:10.0pt;mso-bidi-font-size:12.0pt;
  line-height:107%">7 5 8 6 2 1 9 3 4 </span></p>
  </td>
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:3.0pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:36;height:20.6pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:20.6pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">59.7131 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:37;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:1.3pt;text-align:left;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">Time taken </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:38;height:18.65pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:18.65pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.0771 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:39;height:14.2pt">
  <td width="139" rowspan="2" valign="top" style="width:104.15pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:2.75pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:.7pt 2.7pt 0in 5.35pt;height:14.2pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.4pt;text-align:left;text-indent:0in;
  line-height:107%">Is consistent </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:40;mso-yfti-lastrow:yes;height:22.1pt">
  <td width="95" valign="top" style="width:71.1pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;mso-border-top-alt:
  solid black .5pt;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  padding:.7pt 2.7pt 0in 5.35pt;height:22.1pt">
  <p class="MsoNormal" align="left" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:left;text-indent:0in;
  line-height:107%">0.012 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
</tbody></table>
<br>
<br>
<table class="TableGrid" border="0" cellspacing="0" cellpadding="0" width="623" style="width:467.45pt;margin-left:.3pt;border-collapse:collapse;mso-yfti-tbllook:
 1184;mso-padding-alt:2.85pt 5.75pt 0in 5.75pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.2pt">
  <td width="156" valign="top" style="width:116.8pt;border:solid black 1.0pt;
  mso-border-alt:solid black .5pt;background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;
  height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.1pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Algorithms </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Best Time </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Worst Time </p>
  </td>
  <td width="156" valign="top" style="width:116.85pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;height:14.2pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Average Time </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.3pt">
  <td width="156" valign="top" style="width:116.8pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.35pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Backtracking </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.1pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.961 <span class="SpellE">ms</span> </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin:0in;text-align:center;
  text-indent:0in;line-height:107%">2745 <span class="SpellE">ms</span> </p>
  </td>
  <td width="156" valign="top" style="width:116.85pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:0in;
  margin-bottom:0in;margin-left:.05pt;text-align:center;text-indent:0in;
  line-height:107%">420 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.3pt">
  <td width="156" valign="top" style="width:116.8pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.25pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">Forward-Checking </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.1pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.0366 <span class="SpellE">ms</span> </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.127 <span class="SpellE">ms</span> </p>
  </td>
  <td width="156" valign="top" style="width:116.85pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.0529 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;mso-yfti-lastrow:yes;height:14.3pt">
  <td width="156" valign="top" style="width:116.8pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .5pt;mso-border-alt:solid black .5pt;
  background:#E7E6E6;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.1pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">MAC </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.1pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.008 <span class="SpellE">ms</span> </p>
  </td>
  <td width="156" valign="top" style="width:116.9pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.15pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.023 <span class="SpellE">ms</span> </p>
  </td>
  <td width="156" valign="top" style="width:116.85pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .5pt;mso-border-left-alt:solid black .5pt;
  mso-border-alt:solid black .5pt;padding:2.85pt 5.75pt 0in 5.75pt;height:14.3pt">
  <p class="MsoNormal" align="center" style="margin-top:0in;margin-right:.05pt;
  margin-bottom:0in;margin-left:0in;text-align:center;text-indent:0in;
  line-height:107%">0.0117 <span class="SpellE">ms</span> </p>
  </td>
 </tr>
</tbody></table>
<br>
<br>

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


**Shoutout to my colleague Yousef Hamad Al-Khuraiji and Dr. Hachmi Nasser for contributing in this project**
