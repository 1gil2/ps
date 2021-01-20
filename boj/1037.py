#silver 5

n = input()
L = list(map(int, input().split()))
L.sort()
print(L[0]*L[-1])
