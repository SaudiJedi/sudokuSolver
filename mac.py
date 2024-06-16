import generate_sudoku


def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def ac3(grid, row, col, num):
    for i in range(9):
        if i != row and grid[i][col] == num:
            return False
        if i != col and grid[row][i] == num:
            return False
    box_start_row = 3 * (row // 3)
    box_start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + box_start_row][j + box_start_col] == num and (i + box_start_row != row or j + box_start_col != col):
                return False
    return True


def mac(grid, row=0, col=0):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return mac(grid, row, col + 1)
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num) and ac3(grid, row, col, num):
            grid[row][col] = num
            if mac(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False
