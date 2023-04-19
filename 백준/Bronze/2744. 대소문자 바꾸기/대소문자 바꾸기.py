W = input()
w = ''
for i in W:
    if i.isupper():
        w += i.lower()
    else:
        w += i.upper()
print(w)