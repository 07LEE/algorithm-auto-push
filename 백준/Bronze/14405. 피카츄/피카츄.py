n = input()
n = n.replace('pi', '*').replace('ka', '*').replace('chu', '*')
n = n.replace('*', '')
print('YES') if len(n) == 0 else print('NO')