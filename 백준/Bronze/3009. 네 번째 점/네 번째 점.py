x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list(map(int, input().split()))
answer = []
answer.append(z[0]) if x[0] == y[0] else answer.append(x[0]) if y[0] == z[0] else answer.append(y[0])
answer.append(z[1]) if x[1] == y[1] else answer.append(x[1]) if y[1] == z[1] else answer.append(y[1])
print(answer[0], answer[1])