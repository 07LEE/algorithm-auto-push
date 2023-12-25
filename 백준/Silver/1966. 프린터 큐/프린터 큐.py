T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    printing = 0
    while len(list_N) != 0:
        max_num = max(list_N)
        min_num = min(list_N)
        check = list_N.pop(0)
        if M == 0 and max_num <= check:
            print(printing + 1)
            break
        elif M != 0 and max_num <= check:
            printing += 1
            if M <= 0:
                M = len(list_N) - 1
            else:
                M -= 1
        else:
            list_N.append(check)
            if M <= 0:
                M = len(list_N) - 1
            else:
                M -= 1