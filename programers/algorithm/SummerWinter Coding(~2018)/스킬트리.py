#level 2


def solution(skill, skill_trees):
    answer = 0
    D = dict(zip(skill, range(len(skill))))

    for skill_tree in skill_trees:
        idx = 0
        flag = True
        for s in skill_tree:
            if s in skill:
                if D[s] == idx:
                    idx += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer
