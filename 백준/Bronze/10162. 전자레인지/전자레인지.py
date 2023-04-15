T = int(input())

if T%10 != 0:
	print(-1)
else:
	for i in [300, 60, 10]:
		print(T//i, end=' ')
		T = T%i