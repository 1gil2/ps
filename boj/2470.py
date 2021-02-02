#gold 5

n = int(input())
A = list(map(int, input().split()))
A.sort()

l = 0
r = n-1

m = 2000000001
temp = 0
a = 0
b = 0

while l < r:
    temp = abs(A[l]+A[r])
    if m > temp:
        m = temp
        a = l
        b = r
    if A[l]+A[r] > 0:
        r -= 1
    elif A[l]+A[r] < 0:
        l += 1
    else:
        break

print(A[a], A[b])
