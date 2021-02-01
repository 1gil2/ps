#bronze 2

n = input()
l = len(n)*9
m = int(n)


def disum(a):
    if a == 0:
        return 0
    return a % 10+disum(a//10)


for x in range(m-l, m):
    if x < 0:
        continue
    if x+disum(x) == m:
        print(x)
        break
else:
    print(0)
