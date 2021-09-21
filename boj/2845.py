#bronze 5

import sys
input = sys.stdin.readline

l, p = map(int, input().split())
people = list(map(int, input().split()))

temp = l*p

for person in people:
    print(person - temp, end = ' ')