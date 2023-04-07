def solution(array, n):
    array = sorted(array)
    answer = array[0]
    diff = abs(answer - n)
    
    for x in array:
        curr_diff = abs(x - n)
        if curr_diff < diff:
            answer = x
            diff = curr_diff
            
    return answer