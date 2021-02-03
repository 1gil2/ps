#bronze 1

import sys

D = [0, 1]
for x in range(int(sys.stdin.readline())-1):
    D.append(D[-1]+D[-2])

print(D[-1])
