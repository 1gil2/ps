#bronze 4

s, k, h = map(int, input().split())
m = min(s, k, h)
if s+k+h >= 100:
    print("OK")
else:
    if m == s:
        print("Soongsil")
    elif m == k:
        print("Korea")
    else:
        print("Hanyang")
