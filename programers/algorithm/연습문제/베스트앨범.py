#level 3


def solution(genres, plays):
    answer = []
    Dic1 = {} #
    Dic2 = {}

    lg = len(genres)
    for i in range(lg):
        Dic1[genres[i]] = Dic1.get(genres[i], 0) + plays[i]
        Dic2[genres[i]] = Dic2.get(genres[i], []) + [(plays[i], i)]
    print(Dic1)
    print(Dic2)
    genreSort = sorted(Dic1.items(), key=lambda x: x[1], reverse=True)
    print(genreSort)
    for (genre, totalPlay) in genreSort:
        Dic2[genre] = sorted(Dic2[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in Dic2[genre][:2]]

    return answer
