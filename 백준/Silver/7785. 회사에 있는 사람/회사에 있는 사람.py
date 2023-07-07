import sys
input = sys.stdin.readline

t = int(input())
people = {}
for _ in range(t):
    a, b = input().split()
    if b == 'enter' :
        people[a] = b
    else :
        del people[a]

people = sorted(people, reverse=True)

for i in people:
    print(i)