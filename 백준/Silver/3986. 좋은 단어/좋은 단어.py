N = int(input())
ans = 0

for _ in range(N):
    w = input()
    stack = []
    if len(w)%2 == 0:
        for i in range(len(w)):
            if stack and w[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(w[i])
        if not stack:
            ans += 1        
print(ans)