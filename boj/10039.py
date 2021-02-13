#bronze 4

total = 0
for x in range(5):
    a = int(input())
    if a < 40:
        total += 40
    else:
        total += a

print(int(total/5))
