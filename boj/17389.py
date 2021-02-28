#bronze 2

n = int(input())
s = input()
cnt = 0
score = 0
for x in range(n):
    if s[x] == 'O':
        score += x+1+cnt
        cnt += 1
    else:
        cnt = 0
print(score)
