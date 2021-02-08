#silver 4

while True:
    c1 = []
    flag = True
    st = input()
    if st == '.':
        break
    for x in st:
        if x == '(':
            c1 += x
        elif x == ')':
            if len(c1) == 0:
                flag = False
                break
            if c1[-1] == '(':
                c1.pop(-1)
            else:
                flag = False
                break
        elif x == '[':
            c1 += x
        elif x == ']':
            if len(c1) == 0:
                flag = False
                break
            if c1[-1] == '[':
                c1.pop(-1)
            else:
                flag = False
                break
    if len(c1) == 0 and flag:
        print("yes")
    else:
        print("no")
