import math
N = int(input())
N_list = list(map(int, input().split()))
Y = sum([10 + math.floor((i)/30)*10 for i in N_list])
M = sum([15 + math.floor((i)/60)*15 for i in N_list])
print(f'Y {Y}') if Y < M else print(f'M {M}') if M < Y else print(f'Y M {Y}')