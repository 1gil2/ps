#silver 3

n, m = map(int, input().split())
L = list(map(int, input().split()))
cnt = 0
total = 0
k = 0
for x in L:
    total += x
    if total >= m:
        while total >= m:
            if total == m:
                cnt += 1
            total -= L[k]
            k += 1
print(cnt)
