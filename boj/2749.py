#gold 2


def mulmat(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0]*B[0][0]+A[0][1]*B[1][0]) % 1000000
    C[0][1] = (A[0][0]*B[0][1]+A[0][1]*B[1][1]) % 1000000
    C[1][0] = (A[1][0]*B[0][0]+A[1][1]*B[1][0]) % 1000000
    C[1][1] = (A[1][0]*B[0][1]+A[1][1]*B[1][1]) % 1000000
    return C


E = [[0, 1], [1, 1]]
D = [[1, 0], [0, 1]]

n = int(input())

num2 = []

while True:
    num2.append(n % 2)
    n //= 2
    if n == 0:
        break

a = len(num2)

dp = []
dp.append(E)
for x in range(a-1):
    dp.append(mulmat(dp[-1], dp[-1]))

for x in range(a):
    if num2[x] == 1:
        D = mulmat(D, dp[x])

print(D[0][1])
