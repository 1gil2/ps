#gold 1

import sys
input = sys.stdin.readline


'''
def print_tree():
    for x in range(Level+1):
        for y in range(2**x):
            print(tree[y+2**x], end=' ')
        print()
'''


def level(a):
    cnt = 0
    while a > 0:
        a //= 2
        cnt += 1
    return cnt


def my_sum(root, l, r, s, e):
    if r < s or e < l:
        return 0
    if s <= l and r <= e:
        return tree[root]
    m = (l+r)//2
    return my_sum(root*2, l, m, s, e) + my_sum(root*2+1, m+1, r, s, e)


n, m, k = map(int, input().split())
cmd = m+k
arr = []
for x in range(n):
    arr.append(int(input()))

#트리 만들기
Level = level(n-1)
S = 2**Level
tree = [0 for x in range(S*2)]
for x in range(n):
    tree[x+S] = arr[x]
for x in range(S-1, 0, -1):
    tree[x] = tree[2*x] + tree[2*x+1]

for x in range(cmd):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = b + S - 1
        d = c - tree[idx]
        while idx > 0:
            tree[idx] += d
            idx //= 2
    else:
        print(my_sum(1, 1, S, b, c))
