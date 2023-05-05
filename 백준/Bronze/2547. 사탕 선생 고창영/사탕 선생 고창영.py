t = int(input())
for _ in range(t):
    student = []
    n = input()
    n = int(input())
    for _ in range(n):
        student.append(int(input()))
    if sum(student)%n == 0:
        print('YES')
    else:
        print('NO')