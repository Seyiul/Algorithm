from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight = 0

    while len(bridge):
        answer += 1
        bridge_weight -= bridge.popleft()

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                new_weight = truck_weights.popleft()
                bridge.append(new_weight)
                bridge_weight += new_weight
            else:
                bridge.append(0)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
