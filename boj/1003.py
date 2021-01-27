#silver 3

import sys

fibo = [1, 1]
for x in range(38):
    fibo.append(fibo[-1]+fibo[-2])

for x in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a == 0:
        print(1, 0)
    elif a == 1:
        print(0, 1)
    else:
        print(fibo[a-2], fibo[a-1])
