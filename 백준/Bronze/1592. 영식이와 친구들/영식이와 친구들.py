N, M, L = map(int, input().split())
people = [0] * N
num = 0
while M not in people:
    people[num] += 1
    num = (num+L) % N
print(sum(people)-1)