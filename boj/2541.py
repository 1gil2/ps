#gold 3

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

if a > b:
    flag = 1
    diff = a - b
elif a < b:
    flag = 2
    diff = b - a
else:
    flag = 0

if flag:
    while True:
        if diff % 2 == 1:
            break
        diff //= 2

if flag == 1:
    for _ in range(5):
        p, q = map(int, input().split())
        if (p - q) % diff == 0 and (p - q) >= diff:
            print("Y")
        else:
            print("N")
elif flag == 2:
    for _ in range(5):
        q, p = map(int, input().split())
        if (p - q) % diff == 0 and (p - q) >= diff:
            print("Y")
        else:
            print("N")
elif flag == 0:
    for _ in range(5):
        p, q = map(int, input().split())
        if p == q:
            print("Y")
        else:
            print("N")
