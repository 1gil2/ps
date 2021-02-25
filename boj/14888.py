#silver 1


def back(idx, value):
    if idx == n-1:
        global m
        global M
        m = min(m, value)
        M = max(M, value)
    if B[0] > visit[0]:
        visit[0] += 1
        back(idx+1, value+A[idx+1])
        visit[0] -= 1
    if B[1] > visit[1]:
        visit[1] += 1
        back(idx+1, value-A[idx+1])
        visit[1] -= 1
    if B[2] > visit[2]:
        visit[2] += 1
        back(idx+1, value*A[idx+1])
        visit[2] -= 1
    if B[3] > visit[3]:
        visit[3] += 1
        if value > 0:
            back(idx+1, value//A[idx+1])
            visit[3] -= 1
        else:
            back(idx+1, -(-value//A[idx+1]))
            visit[3] -= 1


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

inf = 1000000000

m = inf
M = -inf

visit = [0]*4

back(0, A[0])

print(M)
print(m)
