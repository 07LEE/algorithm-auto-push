n = int(input())
for _ in range(n):
    a, b = input().split()
    print(f"{a} & {b} are anagrams.") if sorted(list(a)) == sorted(list(b)) else print(f"{a} & {b} are NOT anagrams.")