#bronze 3

import math
n = int(input())
print(int((pow((1+math.sqrt(5))/2, n)-pow((1-math.sqrt(5))/2, n))/math.sqrt(5)))
