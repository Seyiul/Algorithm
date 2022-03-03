def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        idx = 0
        for p in progresses:
            if p >= 100:
                idx += 1
            else:
                break
        if idx != 0:
            progresses = progresses[idx:]
            speeds = speeds[idx:]
            answer.append(idx)

    return answer
