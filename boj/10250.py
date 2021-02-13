#bronze 3

T = int(input())
for x in range(T):
    H, W, N = map(int, input().split())
    cnt = 0
    while N > 0:
        N -= H
        cnt += 1
    N += H
    print(cnt+N*100)
