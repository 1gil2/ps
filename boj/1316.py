#silver 5

A = int(input())
cnt = 0
for y in range(A):
    a = input()
    temp = a[0]
    L = [temp]
    for x in a:
        if x == temp:
            continue
        else:
            L.append(x)
            temp = x
    if len(L) == len(set(L)):
        cnt += 1
print(cnt)
