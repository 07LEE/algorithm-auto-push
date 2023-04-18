A = [int(input()) for _ in range(3)]
[print('Error') if sum(A) != 180 else print('Equilateral') if len(set(A)) == 1 else print('Isosceles') if len(set(A)) == 2 else print('Scalene')]