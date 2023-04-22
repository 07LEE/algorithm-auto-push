import math
T = int(input())
for _ in range (T):
    m, n = map(int, input().split())
    n_fac = math.factorial(n)
    m_fac = math.factorial(m)
    print(int(n_fac / (math.factorial(n - m) * m_fac)))