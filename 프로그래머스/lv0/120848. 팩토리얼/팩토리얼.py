def solution(n):
    num = 1

    for i in range(1, n+1):
        num = num * i
        
        if num == n:
            return i
        if num > n:
            return i-1