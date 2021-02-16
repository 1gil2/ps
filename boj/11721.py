#bronze 2

a = str(input())
le = int(len(a)/10)
for x in range(le):
    print(a[10*x:10*(x+1)])
print(a[10*le:])
