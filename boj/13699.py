#silver 4


def tn(n):
    result = 0
    for x in range(n):
        result += t[x]*t[n-x-1]
    return result


t = [1]
n = int(input())
for x in range(1, n+1):
    t.append(tn(x))

print(t[-1])
