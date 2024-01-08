from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

picture = []
DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(x, y):
    count = 1
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for a, b in DIRECTIONS:
            nx, ny = x + a, y + b
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] is False:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1

    return count

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] is False:
            picture.append(bfs(i, j))

if len(picture) == 0:
    print(0)
    print(0)
else:
    print(len(picture))
    print(max(picture))