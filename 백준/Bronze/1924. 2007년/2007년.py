week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
ans = 0
for i in range(0,x-1):
	ans += day[i]
ans = (ans+ y)%7
print(week[ans])