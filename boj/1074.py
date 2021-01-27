#silver 1

import math


def ser(N, r, c):
    if N == 1:
        return 2*r + c

    a = math.pow(2, N-1)
    if 0 <= r < a and 0 <= c < a:
        return ser(N-1, r, c)
    elif 0 <= r < a and a <= c < a*2:
        return ser(N-1, r, c-a)+a*a
    elif a <= r < a*2 and 0 <= c < a:
        return ser(N-1, r-a, c)+2*a*a
    else:
        return ser(N-1, r-a, c-a)+3*a*a


N, r, c = map(int, input().split())
print(int(ser(N, r, c)))
