#silver 2


def ac(cmd, n, X):
    cmd.replace('RR', '')
    l, r, d = 0, 0, True

    for x in cmd:
        if x == 'R':
            d = not d
        elif x == 'D':
            if d:
                l += 1
            else:
                r += 1

    if l+r <= n:
        ans = X[l:n-r]
        if d:
            return '['+','.join(ans)+']'
        else:
            return '['+','.join(ans[::-1])+']'
    else:
        return 'error'


t = int(input())

for _ in range(t):
    cmd = input()
    n = int(input())
    X = input().rstrip()[1:-1].split(',')

    if n == 0:
        X = []

    print(ac(cmd, n, X))
