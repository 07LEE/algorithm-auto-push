T = int(input())
for _ in range(T):
	N = int(input())
	N_dic = {}
	for _ in range(N):
		a, b = input().split(); N_dic[a] = int(b)
	print(max(N_dic, key=N_dic.get))