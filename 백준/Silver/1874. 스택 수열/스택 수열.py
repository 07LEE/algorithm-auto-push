n = int(input())
stack = []
answer = []
dump = 1
flag = 0

for i in range(n):
    num = int(input())

    while dump <= num:
        stack.append(dump)
        answer.append('+')
        dump += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)