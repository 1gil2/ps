#silver 5

n = int(input())
key = '666'
code = 666

while n:
    if key in str(code):
        n -= 1

    code += 1

print(code-1)
