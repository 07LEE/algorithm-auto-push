num = [int(input()) for _ in range(4)]
if num[0] == 8 or num[0] == 9:
    if num[1] == num[2]:
        if num[3] == 8 or num[3] == 9:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else :
    print('answer')