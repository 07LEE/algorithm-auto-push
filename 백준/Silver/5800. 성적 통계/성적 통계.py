k = int(input())
for i in range(k):
    n = sorted(list(map(int, input().split()))[1:])
    a, b, c= max(n), min(n), 0
    for j in range(len(n)-1):
        if n[j+1] - n[j] > c:
            c = n[j+1] - n[j]
    print(f'Class {i+1}')
    print(f'Max {a}, Min {b}, Largest gap {c}')