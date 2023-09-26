n_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
n = int(input())
for _ in range(n):
    a = int(input())
    ans = False
    for i in range(len(n_list)):
        for j in range(i,len(n_list)):
            if n_list[i] + n_list[j] == a:
                ans = True
                break
    print('Yes') if ans else print('No')