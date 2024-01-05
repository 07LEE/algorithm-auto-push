N = input()
n = len(N)
fac = [i for i in range(1, int(n**0.5)+1) if n % i == 0]
R = fac[-1]
C = n // R

mails = [[] for _ in range(R)]

cnt = 0
for i in range(C) :
    for k in range(R) :
        mails[k].append(N[cnt])
        cnt +=1

for i in range(R) :
    print(''.join(mails[i]), end='')