#bronze 5

D = input().split()
A = int(D[0])
B = int(D[1])
C = int(D[2])
print((A+B) % C)
print((A % C+B % C) % C)
print((A*B) % C)
print(((A % C)*(B % C)) % C)

