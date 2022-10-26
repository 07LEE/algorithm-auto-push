T = 10
for t in range(1, T + 1):
    n = int(input())
    check = input()
    word = input()
    print('#%d %d'%(t,word.count(check)))