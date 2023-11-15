while True:
    try:
        n = int(input())
        ans = ['-']
        for i in range(n):
            tmp = ans[-1]
            blank = ' ' * len(tmp)
            ans.append(f'{tmp}{blank}{tmp}')
        print(ans[n])
    except EOFError:
        break