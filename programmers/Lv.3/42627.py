import heapq


def solution(jobs):
    answer = 0
    time = 0
    start = -1
    i = 0
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = time
            time += current[0]
            answer += (time - current[1])
            i += 1
        else:
            time += 1
    return int(answer/len(jobs))
