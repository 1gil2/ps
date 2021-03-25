#silver 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
robot = [0 for x in range(n)]

time = 0
while True:
    time += 1

    # 1
    A = [A[-1]] + A[:-1]
    robot = [0] + robot[:-1]

    # 2
    for x in range(n - 1, 0, -1):
        if x == n - 1:
            robot[x] = 0
        else:
            if robot[x] == 1 and robot[x + 1] == 0 and A[x + 1] > 0:
                A[x + 1] -= 1
                robot[x] = 0
                robot[x + 1] = 1

    # 3
    if A[0] != 0:
        robot[0] = 1
        A[0] -= 1

    # 4
    if A.count(0) >= k:
        break

print(time)
