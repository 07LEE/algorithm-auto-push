n = int(input())
p = []
for _ in range(n):
    p.append(input()[0])

q = set(p)
fn = []
for i in q:
    if p.count(i) >= 5:
        fn.append(i)

fn = sorted(fn)
if len(fn) == 0:
    print('PREDAJA')
else:
    print(''.join(fn))