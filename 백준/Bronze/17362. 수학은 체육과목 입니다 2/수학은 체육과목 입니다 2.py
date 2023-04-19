n = int(input())%8
print(1) if n == 1 else print(2) if n in [2,0] else print(3) if n in [3,7] else print(4) if n in [4,6] else print(5)