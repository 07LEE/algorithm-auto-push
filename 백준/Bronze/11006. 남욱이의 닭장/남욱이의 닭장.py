t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(f'{(2*m)-n} {m-((2*m)-n)}')