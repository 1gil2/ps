#gold 2

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

k, n = map(int, input().split())
primes = list(map(int, input().split()))

heap = []
for prime in primes:
    heappush(heap, prime)

while n:
    n -= 1

    temp = heappop(heap)

    for prime in primes:
        heappush(heap, temp*prime)

        if temp % prime == 0:
            break

print(temp)
