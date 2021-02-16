#silver 3

dp = [1, 3]
n = int(input())
if n == 1:
    print(1)
else:
    for x in range(2, n):
        dp.append(dp[-1]+2*dp[-2])
    print(dp[-1] % 10007)
