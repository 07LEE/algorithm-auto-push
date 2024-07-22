N = int(input())
for _ in range(N):
    case = input()
    depth = 0
    tree = []
    for i in case:
        if i == ']':
            depth = max(len(tree), depth)
            tree.pop()
        else:
            tree.append('[')
    print(2**depth)