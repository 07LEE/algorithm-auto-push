T = int(input())
for t in range(1, T + 1):
    answer = 1
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    for i in sudoku:
        if len(set(i)) != len(i):
            answer = 0
            break

    for i in range(9):
        check = []
        for j in range(9):
            check.append(sudoku[j][i])
        if len(set(check)) != len(check):
            answer = 0
            break
            
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []

            for a in range(3):
                for b in range(3):
                    check.append(sudoku[i+a][j+b])

            if len(set(check)) != len(check):
                answer = 0
                break           

    print('#%s'%t, answer)