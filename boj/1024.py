#silver 3

n, l = map(int, input().split())

while True:
    if l > 100:
        print(-1)
        break
    t = (l-1)*l//2
    if (n-t)%l == 0 and (n-t)//l >= 0:
        k = (n-t)//l
        for x in range(l):
            print(k+x, end=' ')
        break
    l += 1
