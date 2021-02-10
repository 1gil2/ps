#bronze 2

a = int(input())
for x in range(a):
    ox = input()
    cnt = 0
    total = 0
    for y in ox:
        if y == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)
