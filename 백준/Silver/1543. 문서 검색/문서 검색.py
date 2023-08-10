a = input()
b = input()
c = ''
for i in a.split(b):
    c += i

print((len(a)-len(c))//len(b))