n = int(input())
m = [0, 1]
o = [0, 4]
for i in range(1, n):
    m.append(m[i] + m[i-1])
    o.append(m[i+1]*2 + o[i])
print(o[-1])