import sys
input = sys.stdin.readline

max_value = 0
max_row = 0
max_column = 0

for row in range(1, 10):
    li = list(map(int, input().split()))
    if max(li) > max_value:
        max_value = max(li)
        max_row = row
        max_column = li.index(max_value) + 1

print(max_value)
if max_row == 0 and max_column == 0:
    print(1, 1)
else:
    print(max_row, max_column)