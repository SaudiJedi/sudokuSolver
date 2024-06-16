import generate_sudoku


def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True


def forward_checking(grid, row, col, domain=None):
    if domain is None:
        domain = [None]
    if row == 0 and col == 0:
        domain = [[list(range(1, 10)) for _ in range(9)] for _ in range(9)]

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return forward_checking(grid, row, col + 1, domain)

    for num in domain[row][col]:
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            domain_copy = [row[:] for row in domain]
            domain_copy[row][col] = [num]

            if forward_checking(grid, row, col + 1, domain_copy):
                return True

        grid[row][col] = 0

    return False


