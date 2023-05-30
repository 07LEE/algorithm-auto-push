n, m = map(int, input().split())
board = []
ans = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        drow = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0 :
                    if board[a][b] =='B':
                        drow += 1
                else :
                    if board[a][b] =='W':
                        drow += 1
        
        ans.append(min(drow, 64-drow))

print(min(ans))