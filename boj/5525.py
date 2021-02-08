#silver 2

n = int(input())
m = int(input())
S = input()
S += 'OO'

a = [0 for x in range(m+3)]
i = 0
while i < m:
    if S[i] == 'O':
        i += 1
    if S[i] == 'I':
        cnt = 0
        while True:
            if i+2 < m and S[i+1] == 'O' and S[i+2] == 'I':
                cnt += 1
                i += 2
            else:
                a[i] = cnt
                i += 1
                break

answer = 0
for x in range(m+3):
    if a[x] >= n:
        answer += a[x]-n+1

print(answer)
