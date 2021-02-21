#silver 5


def check():
    lq = len(q)
    if lq != len(u):
        return print(-1)
    if lq != len(a):
        return print(-1)
    if lq != len(c):
        return print(-1)
    if lq != len(k):
        return print(-1)
    for x in range(lq):
        if q[x] > u[x] or u[x] > a[x] or a[x] > c[x] or c[x] > k[x]:
            return print(-1)
    mx = 1
    st = 0
    for x in range(1, lq):
        while k[st] < q[x]:
            st += 1
        mx = max(mx, x - st + 1)
    return print(mx)


duck = input()
le = len(duck)

q = []
u = []
a = []
c = []
k = []

for x in range(le):
    if duck[x] == 'q':
        q.append(x)
    if duck[x] == 'u':
        u.append(x)
    if duck[x] == 'a':
        a.append(x)
    if duck[x] == 'c':
        c.append(x)
    if duck[x] == 'k':
        k.append(x)

check()