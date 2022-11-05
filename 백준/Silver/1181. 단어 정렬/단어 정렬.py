N = int(input())
name = sorted(list(set([input() for _ in range(N)])))
name = sorted(name, key=len)
[print(i) for i in name]