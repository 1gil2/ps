#gold 4

import sys
input = sys.stdin.readline

trees = {}
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    cnt += 1

tree_list = list(trees.keys())
tree_list.sort()
for tree in tree_list:
    print('%s %.4f' %(tree, trees[tree]/cnt*100))
