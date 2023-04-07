def solution(n):
    numbers = [True] * (n+1)
    count = 0
    
    for i in range(2, int(n**0.5)+1):
        if numbers[i] == True:
            for j in range(i*i, n+1, i):
                numbers[j] = False
                
    for i in range(2, n+1):
        divisor_count = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                divisor_count += 1
                if i // j != j:
                    divisor_count += 1
        if divisor_count >= 3 and not numbers[i]:
            count += 1
    
    answer = count
    return answer