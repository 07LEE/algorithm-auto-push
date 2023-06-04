n, a, b = map(int, input().split())
print('Bus') if a < b else print('Anything') if a == b else print('Subway')