import sys
input = sys.stdin.read

li = [0] * 26
word = input().replace('\n', '').replace(' ','')

for i in word:
    li[ord(i) - 97] += 1

for i in range(26):
    if li[i] == max(li):
        print(chr(97 + i), end ='')