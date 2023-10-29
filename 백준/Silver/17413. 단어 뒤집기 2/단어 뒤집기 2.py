import sys
input = sys.stdin.readline

s = input()
c = 0
t = ''
ans = ''

for i in range(len(s)):
    if c == 0:
        if s[i] == ' ':
            ans += t[::-1] + ' '
            t = ''
        elif s[i] == '<':
            c = 1
            ans += t[::-1]
            t = s[i]
        else:
            t += s[i]
            if i == len(s)-1:
                ans += t[::-1].strip()

    elif c == 1:
        t += s[i]

        if s[i] == '>':
            c = 0
            ans += t
            t = ''

print(ans)