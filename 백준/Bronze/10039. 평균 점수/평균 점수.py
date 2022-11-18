ans = []
for _ in range(5):
	num = int(input())
	if num < 40 :
		num = 40
	ans.append(num)
print(sum(ans)//5)