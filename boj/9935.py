#gold 4


def check(st1, st2):
    for x in range(1, len(st2) + 1):
        if st1[-x] != st2[-x]:
            return False
    return True


st = input()
bomb = input()
bl = len(bomb)
temp = ""

stack = []

for s in st:
    stack.append(s)
    if len(stack) < bl:
        continue
    if check(stack, bomb):
        for x in range(bl):
            stack.pop()

if len(stack):
    print("".join(stack))
else:
    print("FRULA")
