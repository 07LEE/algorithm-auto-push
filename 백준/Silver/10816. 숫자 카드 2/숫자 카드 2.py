import collections
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

card_cnt = collections.defaultdict(int)
for card in cards:
    card_cnt[card] += 1

result = [card_cnt[target] for target in targets]
print(*result)