people = 0
ple = []

for _ in range(10):
    a, b = map(int, input().split())
    people -= a
    people += b
    ple.append(people)

print(max(ple))
