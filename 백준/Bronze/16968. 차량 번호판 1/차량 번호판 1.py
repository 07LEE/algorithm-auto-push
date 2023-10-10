s = input()

if s[0] == 'c':
    ans = 26
else:
    ans = 10

for i in range(1, len(s)):
    if s[i] == 'c':
        if s[i - 1] == 'c':
            ans *= 25
        else:
            ans *= 26
    else:
        if s[i - 1] == 'd':
            ans *= 9
        else:
            ans *= 10

print(ans)