#gold 4

op = ['+', '-', '*', '/', '(', ')']

st = input()
ls = len(st)

ans = ''
temp = []

idx = 0

while idx < ls:
    if st[idx] in op:
        if st[idx] == '(':
            temp.append(st[idx])
        elif st[idx] == ')':
            while temp and temp[-1] != '(':
                ans += temp.pop()
            temp.pop()
        elif st[idx] == '*' or st[idx] == '/':
            while temp and (temp[-1] == '*' or temp[-1] == '/'):
                ans += temp.pop()
            temp.append(st[idx])
        else:
            while temp and temp[-1] != '(':
                ans += temp.pop()
            temp.append(st[idx])
    else:
        ans += st[idx]

    idx += 1

while temp:
    ans += temp.pop()

print(ans)