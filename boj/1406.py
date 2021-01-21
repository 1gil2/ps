#silver 3
#pypy3

left = list(input())
right = []
n = int(input())

for x in range(n):
    cmd = list(input().split())
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

st = ''.join(left)+''.join(right[::-1])

print(st)
