#bronze 1

import math

m = int(input())
n = int(input())
total = 0
mini = []
for x in range(m, n+1):
    if math.sqrt(x)-int(math.sqrt(x)) == 0:
       total += x
       mini.append(x)
if total == 0:
    print(-1)
else:
    print(total)
    print(mini[0])
