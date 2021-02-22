#platinum

import bisect
import sys
input = sys.stdin.readline


def lis(arr):
    lis_arr = [arr[0]]
    res = [0]
    for n in arr[1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
            res.append(len(lis_arr)-1)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
            res.append(where)

    i = len(lis_arr)
    print(i)
    ans = []
    for idx in range(len(res)-1, -1, -1):
        if res[idx] == i-1:
            ans.append(arr[idx])
            i -= 1
    for x in range(len(ans)):
        print(ans[-x-1], end=' ')


n = int(input())
arr = list(map(int, input().split()))
lis(arr)
