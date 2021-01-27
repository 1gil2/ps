#level 2


def solution(prices):
    lp = len(prices)
    answer = [0]*lp
    for x in range(lp-1):
        for y in range(x+1, lp):
            answer[x] += 1
            if prices[x] > prices[y]:
                break
    return answer
