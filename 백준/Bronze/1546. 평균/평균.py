n = int(input())
score = list(map(int, input().split()))
a = 0
for i in score:
    a += i/max(score)*100

print(a/n)