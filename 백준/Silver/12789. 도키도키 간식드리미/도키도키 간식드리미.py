n = int(input())
standing = list(map(int, input().split()))
stack = []
target = 1
 
while standing:
    if standing[0] == target:
        standing.pop(0)
        target += 1
    else:
        stack.append(standing.pop(0))
 
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
 
if not stack: 
    print('Nice')
else:
    print('Sad')
 