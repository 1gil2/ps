#gold 5

n, k = map(int, input().split())

N = list(map(int, input()))
temp = []

for x in range(n):
    while temp and temp[-1] < N[x] and k:
        temp.pop()
        k -= 1
    temp.append(N[x])

while k:
    temp.pop()
    k -= 1

for x in temp:
    print(x, end='')

