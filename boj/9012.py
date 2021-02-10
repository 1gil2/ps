#silver 4

T = int(input())
for x in range(T):
    A = input()
    L = []
    flag = True
    for y in A:
        if y == "(":
            L.append("(")
        else:
            if len(L) == 0:
                flag = False
            else:
                L.pop()
    if len(L) == 0:
        flag2 = True
    else:
        flag2 = False
    if flag2:
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
