t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    m = [i for i in n if i%2 == 0 ]
    print(sum(m), min(m))