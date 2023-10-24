n = int(input())
expression = list(input())
num = [int(input()) for i in range(n)]

stack = list()

for i in expression:
    if i.isalpha():
        stack.append(num[ord(i)-65])
    else:
        a = stack.pop()
        result = stack.pop()

        if i == '+':
            result += a

        elif i == '-':
            result -= a

        elif i == '*':
            result *= a

        elif i == '/':
            result /= a

        stack.append(result)

print('%.2f' %stack[-1])
