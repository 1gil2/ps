#gold 5

n = int(input())
m = int(input())

if m != 0:
    num = list(map(int, input().split()))
else:
    num = []

ans = abs(n-100)

for i in range(1000001):
    flag = False
    for x in str(i):
        if int(x) in num:
            flag = True
            break

    if flag:
        continue
    else:
        ans = min(ans, abs(n-i)+len(str(i)))

print(ans)
