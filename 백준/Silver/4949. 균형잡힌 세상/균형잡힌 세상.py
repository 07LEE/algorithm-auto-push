while True:
    stack = []
    string = input()

    if string == '.':
        break

    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')