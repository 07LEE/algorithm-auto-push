def num(n):
    if n == 0:
        return 1
    return n * num(n - 1)

n = int(input())
print(num(n))