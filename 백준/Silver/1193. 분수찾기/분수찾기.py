N = int(input())
line = 1

while N > line:
    N -= line
    line += 1

if line % 2 == 0:
    up = N
    down = line - N + 1
else:
    up = line - N + 1
    down = N

print(up,'/',down, sep="")