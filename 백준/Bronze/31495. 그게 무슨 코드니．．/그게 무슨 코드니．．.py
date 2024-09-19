w = input()
if w[0] != '"' or w[-1] != '"' or len(w) <=2:
    print('CE')
else:
    print(w[1:-1])