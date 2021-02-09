#silver 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solve(s, e):
    if s == e:
        return
    elif s == e - 1:
        print(tree[s])
        return

    node = tree[s]

    temp = s + 1
    while temp < e:
        if tree[temp] > node:
            break
        temp += 1

    solve(s + 1, temp)
    solve(temp, e)
    print(node)


tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

start = 0
end = len(tree)

solve(start, end)
