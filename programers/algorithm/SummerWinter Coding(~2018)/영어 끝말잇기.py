#level 2


def solution(n, words):
    D = dict()

    for idx, word in enumerate(words):
        if idx == 0:
            D[word] = 1
            continue

        if words[idx - 1][-1] != word[0]:
            return [idx % n + 1, idx // n + 1]

        try:
            D[word] += 1
        except:
            D[word] = 1

        if D[word] == 2:
            return [idx % n + 1, idx // n + 1]
    else:
        return [0, 0]
