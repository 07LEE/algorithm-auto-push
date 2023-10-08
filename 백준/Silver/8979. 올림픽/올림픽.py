n, k = map(int, input().split())
lank= [list(map(int, input().split())) for i in range(n)]
lank.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

grade, s = 1, 0

for i in range(n):
    if i != 0:
        if lank[i-1][1:] == lank[i][1:]:
            s += 1
        else :
            if s:
                grade += s
                s = 0
            grade += 1
    if lank[i][0] == k:
        print(grade)
        break