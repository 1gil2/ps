#bronze 1

x, y = map(int, input().split())
day = 0
for k in range(1, x):
    if k == 2:
        day += 28
    elif k in [4, 6, 9, 11]:
        day += 30
    else:
        day += 31
day += y
date = day%7
if date == 1:
    print("MON")
elif date == 2:
    print("TUE")
elif date == 3:
    print("WED")
elif date == 4:
    print("THU")
elif date == 5:
    print("FRI")
elif date == 6:
    print("SAT")
else:
    print("SUN")
