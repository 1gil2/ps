#gold 4

import sys
import math
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

'''
s=['  *  ',' * * ','*****']

def make(side):
    c=len(s)
    for i in range(c):
        s.append(s[i]+" "+s[i])
        s[i]=("   "*side + s[i] + "   "*side)

n=int(input())
k=int(math.log(n//3,2))

for i in range(k):
    make(int(pow(2,i)))

for i in range(n):
    print(s[i])
'''

n = int(input())

stars = [[' ' for x in range(2*n-1)] for y in range(n)]


def fill_star(size, x, y):
    if size == 3:
        stars[y][x] = '*'
        stars[y+1][x-1] = '*'
        stars[y+1][x+1] = '*'
        stars[y+2][x+2] = '*'
        stars[y+2][x+1] = '*'
        stars[y+2][x] = '*'
        stars[y+2][x-1] = '*'
        stars[y+2][x-2] = '*'

    else:
        new_size = size//2
        fill_star(new_size, x, y)
        fill_star(new_size, x-new_size, y+new_size)
        fill_star(new_size, x+new_size, y+new_size)


fill_star(n, n-1, 0)
for k in stars:
    print(''.join(k))
