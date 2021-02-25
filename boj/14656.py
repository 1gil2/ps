#bronze 3

n = int(input())
num = list(map(int,input().split()))
cnt = 0
for x in range(n):
    if num[x] != x+1:
        cnt += 1
print(cnt)
