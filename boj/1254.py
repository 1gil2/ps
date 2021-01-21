#silver 1

s = input()
n = len(s)

for x in range(n):
    if s[x:] == s[x:][::-1]:
        print(n+x)
        break
