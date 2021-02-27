#bronze 1

n = int(input())
song = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']
a = song[(n-1) % 14]
b = n//14
if 'tu' in a:
    for x in range(b):
        a += 'ru'

if len(a) > 11:
    print("tu+ru*", (len(a)-2)//2, sep='')
else:
    print(a)
