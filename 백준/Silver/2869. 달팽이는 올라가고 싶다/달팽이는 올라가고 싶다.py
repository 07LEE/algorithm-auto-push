a, b, v = map(int, input().split())
print((v-a)//(a-b)+1 if (v-a)%(a-b)==0 else (v-a)//(a-b)+2)