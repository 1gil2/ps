#silver 1

fibo = [0, 1]
d, k = map(int, input().split())
for x in range(d-2):
    fibo.append(fibo[-1]+fibo[-2])

b = k//fibo[-1]
while True:
    m = k-fibo[-1]*b
    if m % fibo[-2] == 0:
        print(m//fibo[-2])
        print(b)
        break
    b -= 1
