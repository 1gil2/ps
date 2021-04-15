#gold 4

s = input()
p = input()
ls = len(s)
lp = len(p)

pi = [0 for x in range(lp)]
j = 0
for i in range(1, lp):
    while j > 0 and p[i] != p[j]:
        j = pi[j-1]
    if p[i] == p[j]:
        j += 1
        pi[i] = j

j = 0
flag = False
for i in range(ls):
    while j > 0 and s[i] != p[j]:
        j = pi[j-1]
    if s[i] == p[j]:
        if j == lp-1:
            flag = True
            break
            j = pi[j]
        else:
            j += 1

if flag:
    print(1)
else:
    print(0)
