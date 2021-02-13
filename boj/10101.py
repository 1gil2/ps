#bronze 4

a = float(input())
b = float(input())
c = float(input())
if a+b+c == 180:
    if a == b:
        if b == c:
            print('Equilateral')
        else:
            print('Isosceles')
    else:
        if b == c:
            print('Isosceles')
        else:
            if a == c:
                print('Isosceles')
            else:
                print('Scalene')
else:
    print('Error')
