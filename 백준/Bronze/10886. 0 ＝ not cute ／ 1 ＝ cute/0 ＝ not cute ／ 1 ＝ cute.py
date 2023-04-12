N = int(input())
answer = N
for _ in range(N):
    answer -= int(input())

print("Junhee is not cute!") if (N-answer) < answer else print("Junhee is cute!")