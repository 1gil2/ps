#gold 2


def mm(n):
    ans = ['0', '0', '1', '7', '4', '2', '6', '8', '10', '18', '22', '20', '28', '68', '88']
    if n < 15:
        return ans[n]

    if n%7 == 3:
        return '200' + '8'*(n//7-2)
    else:
        return ans[n%7+7] + '8'*(n//7-1)


def MM(n):
    if n%2 == 0:
        return '1'*(n//2)
    else:
        return '7'+'1'*((n-3)//2)


t = int(input())
for _ in range(t):
    n = int(input())
    print(mm(n), MM(n))
