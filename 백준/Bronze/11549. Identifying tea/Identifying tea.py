t = int(input())
tea = list(map(int, input().split()))
print(tea.count(t)) if t in tea else print(0)