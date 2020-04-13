t = int(input())
for _ in range(t):
    sudoku = []
    for itr in range(9):
        sudoku.append(list(str(input())))
    sudoku[0][0] = sudoku[1][0]
    sudoku[1][3] = sudoku[2][3]
    sudoku[2][6] = sudoku[3][6]
    sudoku[3][1] = sudoku[4][1]
    sudoku[4][4] = sudoku[5][4]
    sudoku[5][7] = sudoku[6][7]
    sudoku[6][2] = sudoku[7][2]
    sudoku[7][5] = sudoku[8][5]
    sudoku[8][8] = sudoku[0][8]
    for r in sudoku:
        print("".join(r))

