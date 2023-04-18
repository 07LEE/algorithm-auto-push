N, W, H, L = map(int, input().split())
[print((W//L)*(H//L)) if (W//L)*(H//L) <= N else print(N)]