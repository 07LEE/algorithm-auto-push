N = int(input())
t = (N-1984)%60
res = "ABCDEFGHIJKL"[t%12] + str(t%10)
print(res)