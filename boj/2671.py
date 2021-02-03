#gold 5


def check(s):
    ls = len(s)
    idx = 0

    while idx < ls:
        if s[idx] == '0':
            if idx + 1 >= ls:
                return False

            if s[idx + 1] != '1':
                return False
            idx += 2

        else:
            if idx + 3 >= ls:
                return False

            if not (s[idx + 1] == '0' and s[idx + 2] == '0'):
                return False
            idx += 1
            while idx < ls and s[idx] == '0':
                idx += 1

            if idx >= ls:
                return False
            idx += 1

            while idx < ls and s[idx] == '1':
                if idx + 2 < ls and s[idx + 1] == '0' and s[idx + 2] == '0':
                    break
                idx += 1

    return True


st = input()

if check(st):
    print("SUBMARINE")
else:
    print("NOISE")