V = int(input())
S = input()
A = S.count('A')
B = S.count('B')
print('Tie') if A == B else print('A') if A>B else print('B')