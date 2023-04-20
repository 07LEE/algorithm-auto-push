c = list(map(int, input().split()))
print('ascending') if c == sorted(c) else print('descending') if c == sorted(c, reverse=True) else print('mixed')