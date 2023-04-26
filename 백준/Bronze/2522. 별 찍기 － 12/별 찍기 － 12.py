N = int(input())
for i in range(1, N+1):
    print('{0}{1}'.format(' '*(N-i), '*'*i))
for i in range(1, N):
    print('{0}{1}'.format(' '*i, '*'*(N-i)))