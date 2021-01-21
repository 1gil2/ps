#silver 3

input()
a = set(input().split())
b = set(input().split())
print(len(a)+len(b)-len(a.intersection(b))*2)
