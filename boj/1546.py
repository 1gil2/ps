#bronze 1

a = int(input())
A = input().split()
m = 0
for x in A:
    if int(x) >= m:
        m = int(x)
B = []
S = 0
for x in A:
    B.append(100*int(x)/m)
for y in B:
    S += y
print(S/a)
