n = int(input())
m = {i+1:int(input()) for i in range(n)}
max_m = [k for k,v in m.items() if max(m.values()) == v]
cnt = 0

while max_m != [1]:
    if max_m[-1] != 1:
        m[1] += 1
        m[max_m[-1]] -= 1
        max_m = [k for k,v in m.items() if max(m.values()) == v]
        cnt += 1
        
print(cnt)