#bronze 1

a = int(input())
b = a
n = 0
while True:
    x = a%10+int(a/10)
    a = x%10+(a%10)*10
    n += 1
    if a == b:
        print(n)
        break
