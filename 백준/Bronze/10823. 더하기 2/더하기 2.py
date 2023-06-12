num = ''
while True:
    try:
        num += input()
    except:
        break
print(sum(map(int, num.split(','))))