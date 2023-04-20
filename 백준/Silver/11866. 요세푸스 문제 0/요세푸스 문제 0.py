import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = [i for i in range(1, N+1)]
Y = []
answer = ''

while len(X) != 0:
    for i in range(K):
        X.append(X.pop(0))
    Y.append(X.pop(-1))

for i in Y:
    answer += str(i)
    if i != Y[-1]:
        answer += ', '

print(f'<{answer}>')