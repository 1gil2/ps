# silver 1

import sys

input = sys.stdin.readline


def preorder(root):
    if root == -1:
        return
    else:
        print(chr(65 + root), end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root == -1:
        return
    else:
        inorder(tree[root][0])
        print(chr(65 + root), end='')
        inorder(tree[root][1])


def postorder(root):
    if root == -1:
        return
    else:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(chr(65 + root), end='')


tree = [[-1, -1] for x in range(26)]

n = int(input())
for x in range(n):
    a, b, c = map(str, input().split())
    if b != '.':
        tree[ord(a) - 65][0] = ord(b) - 65
    if c != '.':
        tree[ord(a) - 65][1] = ord(c) - 65

preorder(0)
print()
inorder(0)
print()
postorder(0)
