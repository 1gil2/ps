#gold 4

n = int(input())

alpha = [0 for x in range(26)]

for _ in range(n):
    num = input()
    ln = len(num)
    for x in range(ln):
        alpha[ord(num[x]) - ord('A')] += 10**(ln-x-1)

alpha.sort(reverse=True)
ans = 0

for x in range(10):
    ans += alpha[x]*(9-x)

print(ans)
