#bronze 2

import sys
input = sys.stdin.readline

T = int(input())
num = list(map(int, input().split()))

for N in num:
    print(int((N//3)*(N//3+1)/2*3+(N//7)*(N//7+1)/2*7-(N//21)*(N//21+1)/2*21))
