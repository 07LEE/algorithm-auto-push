from collections import deque
N, M = map(int, input().split())
check = list(map(int, input().split()))
deq = deque(list(range(1, N+1)))
ans = 0

def left(n, ans):
    for _ in range(n):
        num = deq.popleft()
        deq.append(num)
        ans += 1
    return ans


def right(n, ans):
    for _ in range(n):
        num = deq.pop()
        deq.appendleft(num)
        ans += 1
    return ans


while check:
    num = check.pop(0)
    idx = deq.index(num)

    if  idx == 0:
        deq.popleft()
    elif idx <= len(deq)/2:
        ans = left(deq.index(num), ans)
        deq.popleft()
    elif idx > len(deq)/2:
        ans = right(len(deq)-deq.index(num), ans)
        deq.popleft()

print(ans)