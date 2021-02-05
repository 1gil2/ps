#bronze 1

c = int(input())
for x in range(c):
    sum1 = 0
    n = input().split()
    for y in n[1:]:
        sum1 += int(y)
    ave = sum1/int(n[0])
    cnt = 0
    for z in n[1:]:
        if int(z) > ave:
            cnt += 1
    print("%0.3f" % (100*cnt/int(n[0])), end='')
    print("%")
