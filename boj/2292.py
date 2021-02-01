#bronze 2

a = int(input())-1
cnt = 1
dg = 1

if a % 6 == 0:
    a = a/6
else:
    a = int(a/6)+1

while a > 0:
    a -= dg
    dg += 1
    cnt += 1
print(cnt)
