N = str(input())
print(int(N[0])+int(N[1])) if len(N) == 2 else print(10+int(N.replace('10', ''))) if len(N) == 3 else print(20)