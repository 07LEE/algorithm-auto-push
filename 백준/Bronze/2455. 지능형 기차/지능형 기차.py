people = 0
ple = []

for _ in range(4):
    a, b = map(int, input().split())
    people -= a
    people += b
    ple.append(people)

print(max(ple))
