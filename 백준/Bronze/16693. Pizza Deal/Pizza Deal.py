from math import pi

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())
A2 = pi * R1 * R1
V1 = A1 / P1
V2 = A2 / P2
print('Slice of pizza') if V1 > V2 else print('Whole pizza')