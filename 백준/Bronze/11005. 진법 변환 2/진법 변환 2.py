N, B = map(int, input().split())
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while N != 0:
    ans += str(tmp[N%B])
    N = N//B

print(ans[::-1])