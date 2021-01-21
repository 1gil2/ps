#silver 3

N = int(input())
D = [0, 0, 1, 1]
for x in range(4, N+1):
    if x%3 == 0:
        if x%2 == 0:
            D.append(min(D[int(x/3)], D[int(x/2)], D[x-1])+1)
        else:
            D.append(min(D[int(x/3)], D[x-1])+1)
    elif x%2 == 0:
        D.append(min(D[int(x/2)], D[x-1])+1)
    else:
        D.append(D[x-1]+1)

print(D[N])
