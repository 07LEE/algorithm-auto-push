while True:
    n = input()
    if n == '0':
        break
    cm = 1 + len(n) * 4
    cm -= n.count('1') 
    cm += n.count('0')
    print(cm)