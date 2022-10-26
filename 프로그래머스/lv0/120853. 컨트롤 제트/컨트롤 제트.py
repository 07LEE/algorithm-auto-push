def solution(s):
    S = s.split()
    stack = []
    for i in range(len(S)):
        stack.pop() if S[i] == 'Z' else stack.append(int(S[i]))
    return sum(stack)
        