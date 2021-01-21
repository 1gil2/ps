#bronze 2

X = int(input())
cnt = 1
while(X > 0):
    X -= cnt
    cnt += 1
if cnt%2 == 1:
    print(X+cnt-1, '/', -X+1, sep='')
else:
    print(-X+1, '/', cnt+X-1, sep='')
