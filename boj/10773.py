#silver 4

A = []
total = 0

for x in range(int(input())):
    a = int(input())
    if a == 0:
        total -= A[-1]
        A.pop()
    else:
        A.append(a)
        total += a

print(total)
