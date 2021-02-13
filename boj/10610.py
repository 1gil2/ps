#silver 5

n = input()
ans = 0
m = []
for x in n:
    m.append(int(x))
if '0' in n:
    for x in n:
        ans += int(x)
    if ans % 3 == 0:
        m = sorted(m, reverse=True)
        for y in m:
            print(y, end='')
    else:
        print(-1)
else:
    print(-1)
