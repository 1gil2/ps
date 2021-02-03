#bronze 1

A = int(input())
count = 0
k = 0
while True:
    if A % 5 == 0:
        break
    A -= 3
    count += 1
    if A < 0:
        print(-1)
        k = 1
        break
if k == 0:
    print(count+int(A/5))
