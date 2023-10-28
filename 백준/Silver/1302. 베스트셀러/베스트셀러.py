import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
a = [input().strip() for _ in range(n)]
a.sort()
print(Counter(a).most_common(n=1)[0][0])