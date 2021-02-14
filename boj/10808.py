#bronze 2

n = str(input())
alpha = []
for x in range(26):
    alpha.append(0)
for x in n:
    alpha[ord(x)-97] += 1
for x in alpha:
    print(x, ' ', end='', sep='')
