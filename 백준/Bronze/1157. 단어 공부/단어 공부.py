s = input().upper()
s_list = list(set(s))
cnt = []

for i in s_list:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(s_list[(cnt.index(max(cnt)))])