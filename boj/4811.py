#gold 5


def alyak(w, h):
    if al[w][h] != -1:
        return al[w][h]
    if w == 0:
        al[w][h] = 1
        return 1
    if h == 0:
        al[w][h] = alyak(w-1, h+1)
    else:
        al[w][h] = alyak(w-1, h+1)+alyak(w, h-1)
    return al[w][h]


al = [[-1]*31 for x in range(31)]

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(alyak(n, 0))
