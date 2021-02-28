#gold 4

from collections import Counter


def rc_sort():
    M = 0
    lA = len(A)

    for x in range(lA):
        a = [i for i in A[x] if i != 0]
        a = Counter(a).most_common()
        a.sort(key=lambda x: (x[1], x[0]))
        A[x] = []
        for m, n in a:
            A[x].append(m)
            A[x].append(n)
        la = len(a)
        if M < la*2:
            M = la*2

    for x in range(lA):
        for y in range(M-len(A[x])):
            A[x].append(0)
        A[x] = A[x][:100]


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for x in range(3)]

for x in range(101):
    try:
        if A[r-1][c-1] == k:
            print(x)
            break
    except:
        pass

    if len(A) < len(A[0]):
        A = list(zip(*A))
        rc_sort()
        A = list(zip(*A))
    else:
        rc_sort()
else:
    print(-1)
