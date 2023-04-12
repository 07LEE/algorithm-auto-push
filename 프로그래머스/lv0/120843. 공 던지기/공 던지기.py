def solution(numbers, K):
    n = len(numbers)
    i = 0 
    for _ in range(K):
        i = (i + 2) % n  
        if i == 0:
            i = n  
    return numbers[i - 2]  