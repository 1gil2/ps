#silver 5

for t in range(int(input())):
    n = int(input())
    pig = sum(list(map(int, input().split())))
    day = 1
    while True:
        if n < pig:
            break
        pig *= 4
        day += 1
    print(day)
