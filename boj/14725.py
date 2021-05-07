#gold 2


def go_trie(tree, key, st):
    child = tree.get(key)
    if child:
        for k in sorted(child.keys()):
            print(st+k)
            if child.get(k):
                go_trie(child, k, st+'--')


n = int(input())

#trie구조 json처럼
tree = dict()

#make trie
for _ in range(n):
    temp = list(input().split())
    k, food = int(temp[0]), temp[1:]

    if not food[0] in tree:
        tree[food[0]] = dict()

    temp = tree
    for i in range(k-1):
        child = temp.get(food[i])

        if child and (food[i+1] in child):
            temp = child
            continue

        child[food[i+1]] = dict()
        temp = child

#print trie
for key in sorted(tree.keys()):
    print(key)
    go_trie(tree, key, '--')
