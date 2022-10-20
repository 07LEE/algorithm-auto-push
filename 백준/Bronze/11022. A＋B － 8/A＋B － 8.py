for i in range(int(input())):
    n = list(map(int, input().split()))
    print('Case #%d: %d + %d ='%(i+1,n[0],n[1]),sum(n))