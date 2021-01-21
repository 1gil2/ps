#gold 4

n = int(input())
k = int(input())

s, e = 0, k
res = 0

while s <= e:
    cnt = 0
    m = (s+e)//2

    for x in range(1, n+1):
        cnt += min(m//x, n)

    if cnt < k:
        s = m+1
    else:
        res = m
        e = m-1

print(res)
