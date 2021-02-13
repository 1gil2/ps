#silver 3

t = int(input())

for _ in range(t):
    a = int(input())
    D = dict()
    for x in range(a):
        item, where = map(str, input().split())

        try:
            D[where] += 1
        except:
            D[where] = 1

    if len(D) == 1:
        print(D[where])
    else:
        ret = 1
        for y in D:
            ret *= D[y]+1
        print(ret-1)
