#silver 1

def bit(x):
    if x == 0:
        return
    bi.append(x % 2)
    bit(x // 2)

a, b, c = map(int, input().split())

bi = []
bit(b)
ai = [a % c]

for x in range(len(bi) - 1):
    ai.append((ai[-1] * ai[-1]) % c)

ans = 1

for x in range(len(bi)):
    if bi[x] == 1:
        ans *= (bi[x] * ai[x])
        ans %= c

print(ans)
