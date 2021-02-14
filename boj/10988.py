#bronze 1


def pel(word):
    if word == word[::-1]:
        print(1)
    else:
        print(0)


word = input()
pel(word)
