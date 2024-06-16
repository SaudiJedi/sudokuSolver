from backtracking import backtracking
from forward_checking import forward_checking
from mac import mac
import generate_sudoku
import timeit

bt = generate_sudoku.generate_sudoku()
fc = bt
m = bt

print('Sudoku Before:')
for i in range(9):
    for j in range(9):
        print(bt[i][j], end=" ")
    print()
print('')

print('Sudoku After:')
bt_time_before = timeit.default_timer()
if backtracking(bt, 0, 0):
    bt_time_after = timeit.default_timer()
    for i in range(9):
        for j in range(9):
            print(bt[i][j], end=" ")
        print()
    print('')
    print('Execution time for backtracking: ', (bt_time_after-bt_time_before)*1000)
else:
    print('No Solution for backtracking')

fc_time_before = timeit.default_timer()
if forward_checking(fc, 0,0):
    fc_time_after = timeit.default_timer()
    print('Execution time for backtracking: ', (fc_time_after - fc_time_before)*1000)
else:
    print('No Solution for forward-checking')


m_time_before = timeit.default_timer()
if mac(m, 0,0):
    m_time_after = timeit.default_timer()
    print('Execution time for MAC: ', (m_time_after - m_time_before)*1000)
else:
    print('Not consistent by MAC')