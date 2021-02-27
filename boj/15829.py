#bronze 2

n = int(input())
s = input()

ans = 0

for x in range(n):
    ans += (pow(31, x)*(ord(s[x])-96)) % 1234567891

print(ans % 1234567891)
