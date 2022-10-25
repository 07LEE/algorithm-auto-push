for _ in range(10):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    starting = int(data[99].index(2))
    i = 0
    while i < 99 :
        if data[99-i][starting] == 1:
            data[99 - i][starting] = 2

        if 0 < starting < 99 :
            if data[99-i][starting+1] == 1:
                starting += 1
                i -= 1

            elif data[99-i][starting-1] == 1:
                starting -= 1
                i -= 1

        elif starting == 0:
            if data[99-i][starting+1] == 1:
                starting += 1
                i -= 1

        elif starting == 99:
            if data[99-i][starting-1] == 1:
                starting -= 1
                i -= 1

        i += 1
    print('#%s %s'%(n, starting))