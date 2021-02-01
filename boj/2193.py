#silver 3

n = int(input())
dp0 = [0, 0]
dp1 = [0, 1]
for x in range(1, n):
    dp0.append(dp0[-1]+dp1[-1])
    dp1.append(dp0[-2])
print(dp0[n]+dp1[n])
