import heapq


def solution(operations):
    answer = []
    for operation in operations:
        op = operation[0]
        num = int(operation[1:])

        if op == 'I':
            heapq.heappush(answer, num)
        elif op == 'D':
            if len(answer) != 0:
                if num >= 0:
                    answer.pop()
                else:
                    heapq.heappop(answer)

    return [max(answer), min(answer)] if len(answer) != 0 else [0, 0]
