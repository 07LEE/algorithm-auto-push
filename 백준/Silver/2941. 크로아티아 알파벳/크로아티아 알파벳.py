N = input()
dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in dic:
    N = N.replace(i, ' ')
print(len(N))