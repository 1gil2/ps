#silver 4

A = int(input())
if A > 99:
    cnt = 99
    for x in range(100, A+1):
        if int(x/100)+int(x%10) == 2*int((x%100)/10):
            cnt += 1
    print(cnt)
else:
    print(A)
