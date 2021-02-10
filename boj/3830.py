#platinum 4

import sys
input = sys.stdin.readline


def my_find(node, w):
    if parent[node] == node:
        return node, w
    return my_find(parent[node], w + weight[node])


def my_uni(a, b, w):
    a_root, aw = my_find(a, 0)
    b_root, bw = my_find(b, 0)

    if size[a_root] > size[b_root]:
        parent[b_root] = a_root
        weight[b_root] -= bw - aw - w
        size[a_root] += size[b_root]
        size[b_root] = 1
    else:
        parent[a_root] = b_root
        weight[a_root] += bw - aw -w
        size[b_root] += size[a_root]
        size[a_root] = 1


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [x for x in range(n+1)]
    size = [1 for x in range(n+1)]
    weight = [0 for x in range(n+1)]

    for _ in range(m):
        cmd = list(input().split())
        if cmd[0] == '!':
            my_uni(int(cmd[1]), int(cmd[2]), int(cmd[3]))
        else:
            x, xw = my_find(int(cmd[1]), 0)
            y, yw = my_find(int(cmd[2]), 0)
            if x == y:
                print(yw-xw)
            else:
                print("UNKNOWN")
