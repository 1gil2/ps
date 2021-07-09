#silver 2

import sys
input = sys.stdin.readline


def go1(st):
    cnt = 1
    st[0] = int(not st[0])
    st[1] = int(not st[1])
    for x in range(1, n):
        if st[x - 1] != st2[x - 1]:
            cnt += 1
            st[x - 1] = int(not st[x - 1])
            st[x] = int(not st[x])
            if x != n - 1:
                st[x + 1] = int(not st[x + 1])

    if st == st2:
        return cnt
    return -1


def go2(st):
    cnt = 0
    for x in range(1, n):
        if st[x - 1] != st2[x - 1]:
            cnt += 1
            st[x - 1] = int(not st[x - 1])
            st[x] = int(not st[x])
            if x != n - 1:
                st[x + 1] = int(not st[x + 1])

    if st == st2:
        return cnt
    return -1


n = int(input())
st1 = list(map(int, input().rstrip()))
st2 = list(map(int, input().rstrip()))

ans1 = go1(st1[:])
ans2 = go2(st1[:])

if ans1 >= 0 and ans2 >= 0:
    print(min(ans1, ans2))
elif ans1 >= 0 and ans2 < 0:
    print(ans1)
elif ans1 < 0 and ans2 >= 0:
    print(ans2)
else:
    print(-1)
