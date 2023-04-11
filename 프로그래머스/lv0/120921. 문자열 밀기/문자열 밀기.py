def solution(A, B):
    if len(A) != len(B):
        return -1
    
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:
            return i

    return -1