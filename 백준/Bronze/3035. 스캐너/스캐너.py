import sys
input = sys.stdin.readline

R, C, ZR, ZC = map(int, input().split())
paper = []
scanner = []
for _ in range(R):
    paper.append(input())

for i in range(R):
    row = []
    for j in range(C):
        row.append(paper[i][j] * ZC)

    for _ in range(ZR):
        scanner.append(row)

for s in scanner:
    print(''.join(s))