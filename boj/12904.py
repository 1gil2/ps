#gold 5

S = input()
T = input()

ls = len(S)
lt = len(T)

for x in range(lt-ls):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]

if T == S:
    print(1)
else:
    print(0)
