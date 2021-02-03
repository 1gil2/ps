#bronze 2

L = list(map(int, input().split()))
up = 0
down = 0
temp = L[0]
for x in L:
    if x == temp:
        continue
    elif x < temp:
        down += 1
    else:
        up += 1
    temp = x
if up == 0:
    print("descending")
elif down == 0:
    print("ascending")
else:
    print("mixed")
