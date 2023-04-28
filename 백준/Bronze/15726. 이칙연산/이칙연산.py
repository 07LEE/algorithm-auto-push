N = list(map(int, input().split()))
print(int(N[0]*N[1]/N[2])) if N[1] > N[2] else print(int(N[0]/N[1]*N[2]))