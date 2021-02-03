#silver 5

a, b = map(int, input().split())
n = a * b
if b > a:
    temp = a
    a = b
    b = temp

while True:
    if a % b == 0:
        break
    a = a % b
    temp = a
    a = b
    b = temp

print(b)
print(int(n / b))
