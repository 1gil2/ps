#gold 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

tot = sys.maxsize
answer = []

for i in range(n-2):
    p2 = i+1
    p3 = n-1

    while p2 < p3:
        temp = arr[i] + arr[p2] + arr[p3]

        if abs(temp) <= abs(tot):
            answer = [arr[i], arr[p2], arr[p3]]
            tot = temp

        if temp < 0:
            p2 += 1
        elif temp > 0:
            p3 -= 1
        else:
            print(*answer)
            sys.exit()

print(*answer)
