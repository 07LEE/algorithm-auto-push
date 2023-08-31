n = int(input())
for _ in range(n):
    dic = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    w = input()
    for i in range(38):
        dic[w[i:i+3]] += 1
    for k, v in dic.items():
        print(v, end=' ')