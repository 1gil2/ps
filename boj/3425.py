#gold 2

import sys
from collections import deque
#input = sys.stdin.readline
inf = 10**9

while True:
    flag = False
    cmd_list = []
    while True:
        cmd = input()
        if cmd == "QUIT":
            flag = True
            break
        elif cmd == "END":
            break
        cmd_list.append(cmd)

    if flag:
        break

    n = int(input())
    for x in range(n):
        stack = deque()
        stack.append(int(input()))

        flag1 = False
        try:
            for cmd in cmd_list:
                if cmd[0] == "N":
                    stack.append(int(cmd.split()[1]))
                elif cmd == "POP":
                    stack.pop()
                elif cmd == "INV":
                    v = stack.pop()
                    v *= -1
                    stack.append(v)
                elif cmd == "DUP":
                    v = stack.pop()
                    stack.append(v)
                    stack.append(v)
                elif cmd == "SWP":
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v1)
                    stack.append(v2)
                elif cmd == "ADD":
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v1+v2)
                elif cmd == "SUB":
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v2-v1)
                elif cmd == "MUL":
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v2*v1)
                elif cmd == "DIV":
                    v1, v2 = stack.pop(), stack.pop()
                    if v1 == 0:
                        raise Exception
                    v3 = abs(v2) // abs(v1)
                    if (v1*v2) < 0:
                        v3 *= -1
                    stack.append(v3)
                elif cmd == "MOD":
                    v1, v2 = stack.pop(), stack.pop()
                    if v1 == 0:
                        raise Exception
                    v3 = abs(v2) % abs(v1)
                    if v3 < 0 < v2 or v2 < 0 < v3:
                        v3 *= -1
                    stack.append(v3)

                if len(stack) >= 1 and abs(stack[-1]) > inf:
                    raise Exception
        except:
            flag1 = True

        if flag1 or len(stack) != 1:
            print("ERROR")
        else:
            print(stack.pop())

    print()
    input()
