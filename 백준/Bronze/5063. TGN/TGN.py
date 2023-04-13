N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    print('does not matter') if r == e-c else print('advertise') if r < e-c else print('do not advertise')