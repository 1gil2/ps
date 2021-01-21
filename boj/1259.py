#bronze 1

while True:
    n = input()
    if n == '0':
        break
    l = len(n)
    le = l//2+1
    flag = True
    for x in range(le):
        if n[x] == n[l-x-1]:
            continue
        else:
            flag = False
            break
    if flag:
        print("yes")
    else:
        print("no")
