c = int(input())
for i in range(int(input())):
    a, b = map(int, input().split())
    c = c-a*b
print('Yes' if c == 0 else 'No')