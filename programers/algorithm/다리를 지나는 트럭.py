#level 2

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    answer = 0
    while bridge:
        bridge.pop(0)
        answer += 1
        if truck_weights:
            if (sum(bridge)+truck_weights[0]) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
