import random


def generate_sudoku():
    base  = 3
    side  = base*base
    nums  = list(range(1, side + 1))
    board = [[None]*side for _ in range(side)]

    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    def shuffle(s): return random.sample(s,len(s))

    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]

    rBase = range(base)
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(nums)

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    squares = side*side
    empties = squares * 3//4
    for p in map(int, random.sample(range(squares),empties)):
        board[p//side][p%side] = 0

    return board
