#silver 4

t=int(input())
for x in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dist=(x1-x2)**2+(y1-y2)**2
    R=r1+r2
    r=abs(r1-r2)
    if  dist==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if dist == R*R or dist == r*r:
            print(1)
        elif dist > R*R or dist < r*r:
            print(0)
        else:
            print(2)