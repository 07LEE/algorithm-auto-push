def solution(s):
    result = [0, 0]
    for _ in range(len(s)):
        result[1] += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]
        result[0] += 1
        if s == '1' :
            return result