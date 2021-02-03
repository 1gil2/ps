#bronze 2

a = int(input())
for x in range(a):
    R, S = input().split()
    st = ''
    for y in S:
        st += y*int(R)
    print(st)
