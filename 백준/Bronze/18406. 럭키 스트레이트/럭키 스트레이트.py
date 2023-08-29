n = str(input())
a, b = n[:len(n)//2], n[len(n)//2:]
print('LUCKY') if sum(map(int, list(a))) == sum(map(int, list(b))) else print('READY')