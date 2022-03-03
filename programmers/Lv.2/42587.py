from collections import deque


def solution(priorities, location):
    answer = 1
    priorities = deque(priorities)

    while len(priorities) != 0:
        if location == 0:
            if priorities[location] == max(priorities):
                return answer
            else:
                location = len(priorities)
        else:
            if priorities[0] == max(priorities):
                answer += 1
                priorities.popleft()
            else:
                priorities.rotate(-1)

            location -= 1

    return answer
