n = int(input())
for _ in range(n):
    a = sorted(list(map(int, input().split()))[1:])
    b = sorted(list(map(int, input().split()))[1:])
    if a == b :
        print('D')
    elif a.count(4) > b.count(4):
        print('A')
    elif b.count(4) > a.count(4):
        print('B')
    else :
        if a.count(3) > b.count(3):
            print('A')
        elif a.count(3) < b.count(3):
            print('B')
        else :
            if a.count(2) > b.count(2):
                print('A')
            elif a.count(2) < b.count(2):
                print('B')
            else :
                if a.count(1) > b.count(1):
                    print('A')
                elif a.count(1) < b.count(1):
                    print('B')