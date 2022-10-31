S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = []
for i in alphabet:
    if i in S:
        ans.append(str(S.index(i)))
    else:
        ans.append('-1')
print(' '.join(ans))