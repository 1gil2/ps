#gold 3

import sys
input = sys.stdin.readline

L = int(input())
ml, mk = map(int, input().split())
c = int(input())
z = []
for x in range(L):
    z.append(int(input()))

flag = True
cur_damage = mk
max_damage = mk*ml

for zombi in z:
    if zombi > cur_damage:
        if c == 0:
            flag = False
            break
        else:
            c -= 1
            max_damage = max(max_damage - mk, mk)
            cur_damage = min(cur_damage, max_damage)
    else:
        cur_damage = min(cur_damage + mk, max_damage)
        max_damage = min(max_damage + mk, mk*ml)

if flag:
    print("YES")
else:
    print("NO")
