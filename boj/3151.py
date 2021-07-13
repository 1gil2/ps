#gold 4

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for x in range(n - 2):
    left = x + 1
    right = n - 1

    temp = arr[x]

    while left < right:

        ans = temp + arr[left] + arr[right]

        if ans == 0:
            if arr[left] == arr[right]:
                cnt += (right - left + 1) * (right - left) // 2
                break
            else:
                right2 = right
                r_cnt = 0
                while arr[right] == arr[right2]:
                    right -= 1
                    r_cnt += 1

                left2 = left
                l_cnt = 0
                while arr[left] == arr[left2]:
                    left += 1
                    l_cnt += 1

                cnt += r_cnt * l_cnt

        elif ans > 0:
            right -= 1
        else:
            left += 1

print(cnt)
