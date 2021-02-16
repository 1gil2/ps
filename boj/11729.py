#silver 2


def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)
# n 개의 원판을 a 에서 c 로 옮기기


move = []
hanoi(int(input()), 1, 2, 3)

l = len(move)
print(l)

for x in range(l):
    print(move[x][0], move[x][1])
