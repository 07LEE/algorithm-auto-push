apples_3p = int(input())
apples_2p = int(input())
apples_1p = int(input())
bananas_3p = int(input())
bananas_2p = int(input())
bananas_1p = int(input())

apples_score = apples_3p * 3 + apples_2p * 2 + apples_1p
bananas_score = bananas_3p * 3 + bananas_2p * 2 + bananas_1p

if apples_score > bananas_score:
    print('A')
elif apples_score < bananas_score:
    print('B')
else:
    print('T')