n = int(input())
a = [(i*2-1) for i in range(1, n+1)]
print(' '.join(map(str, a)))