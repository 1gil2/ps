#bronze 4

n = int(input())
m = input()
for x in m[::-1]:
    print(n*int(x))
print(n*int(m))
