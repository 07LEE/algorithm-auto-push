S, K, H = map(int, input().split())
print('OK') if S+K+H >= 100 else print('Soongsil') if S == min(S, K, H) else print('Korea') if K == min(S, K, H) else print('Hanyang')