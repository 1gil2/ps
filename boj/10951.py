#bronze 3

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break
