n = int(input())
for i in range(n):
    m = int(input())
    t = input()
    if m%2 != 0:
        print(f'#{i+1} No')
    else:
        if t[:(m//2)] == t[(m//2):]:
            print(f'#{i+1} Yes')
        else:
            print(f'#{i+1} No')