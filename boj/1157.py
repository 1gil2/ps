#bronze 1

a = input().upper()
D = dict()
for x in a:
    if x in D:
        D[x] += 1
    else:
        D[x] = 1

mx = 0
mxt = ''
cnt = 1
for x in D:
    if mx < D[x]:
        mx = D[x]
        mxt = x
        cnt = 1
    elif mx == D[x]:
        cnt += 1

if cnt == 1:
    print(mxt)
else:
    print("?")
