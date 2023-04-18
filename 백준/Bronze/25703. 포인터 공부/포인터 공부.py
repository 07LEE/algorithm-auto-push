N = int(input())
[print('int a;') if i == 0 else print('int *ptr = &a;') if i == 1 else print('int **ptr2 = &ptr;') if i == 2 else print('int '+'*'*i+f'ptr{i} = &ptr{i-1};') for i in range(N+1)]