#level 1


def solution(seoul):
    for x in range(len(seoul)):
        if seoul[x] == "Kim":
            return "김서방은 "+str(x)+"에 있다"
