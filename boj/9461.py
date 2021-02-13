#silver 3

for t in range(int(input())):
    p = [0, 1, 1, 1, 2, 2, 3]
    n = int(input())
    if n < 7:
        print(p[n])
    else:
        for x in range(n-6):
            p.append(p[-1]+p[-5])
        print(p[-1])
