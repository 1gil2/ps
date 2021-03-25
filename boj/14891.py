#gold 5


def rotate(idx, vec):
    if vec == 1:
        gear[idx] = gear[idx][-1] + gear[idx][:-1]
    if vec == -1:
        gear[idx] = gear[idx][1:] + gear[idx][0]


gear = []
for _ in range(4):
    gear.append(input())

k = int(input())

for _ in range(k):
    idx, vec = map(int, input().split())
    idx -= 1
    flag1 = (gear[0][2] == gear[1][6])
    flag2 = (gear[1][2] == gear[2][6])
    flag3 = (gear[2][2] == gear[3][6])

    if idx == 0:
        if flag1:
            rotate(0, vec)
        else:
            if flag2:
                rotate(0, vec)
                rotate(1, vec * -1)
            else:
                if flag3:
                    rotate(0, vec)
                    rotate(1, vec * -1)
                    rotate(2, vec)
                else:
                    rotate(0, vec)
                    rotate(1, vec * -1)
                    rotate(2, vec)
                    rotate(3, vec * -1)
    if idx == 1:
        if flag1 == False:
            rotate(0, vec * -1)
        if flag2 == False:
            if flag3:
                rotate(1, vec)
                rotate(2, vec * -1)
            else:
                rotate(1, vec)
                rotate(2, vec * -1)
                rotate(3, vec)
        else:
            rotate(1, vec)

    if idx == 2:
        if flag3 == False:
            rotate(3, vec * -1)
        if flag2 == False:
            if flag1 == False:
                rotate(0, vec)
                rotate(1, vec * -1)
                rotate(2, vec)
            else:
                rotate(1, vec * -1)
                rotate(2, vec)
        else:
            rotate(2, vec)

    if idx == 3:
        if flag3:
            rotate(3, vec)
        else:
            if flag2:
                rotate(3, vec)
                rotate(2, vec * -1)
            else:
                if flag1:
                    rotate(3, vec)
                    rotate(2, vec * -1)
                    rotate(1, vec)
                else:
                    rotate(3, vec)
                    rotate(2, vec * -1)
                    rotate(1, vec)
                    rotate(0, vec * -1)

print(int(gear[0][0]) + int(gear[1][0]) * 2 + int(gear[2][0]) * 4 + int(gear[3][0]) * 8)
