#silver 2

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

esu = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
D = b*b - 4*a*c

if D <= 0:
    print("둘다틀렸근")
    sys.exit()

temp = (D**0.5)
if int(temp) == temp:
    x1 = (-b + temp)/(2*a)
    x2 = (-b - temp)/(2*a)
    if int(x1) == x1 and int(x2) == x2:
        if x1 in esu and x2 in esu:
            print("이수근")
        else:
            print("정수근")
    else:
        print("둘다틀렸근")
else:
    print("둘다틀렸근")
