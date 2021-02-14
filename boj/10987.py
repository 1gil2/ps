#bronze 2

n = str(input())
cnt = 0
for x in n:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        cnt += 1
print(cnt)
