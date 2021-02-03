#bronze 2

n, m = map(int, input().split())
num = list(map(int, input().split()))

temp = 0

for x in range(n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            su = num[x]+num[y]+num[z]
            if su <= m:
                if temp < su:
                    temp = su
print(temp)
