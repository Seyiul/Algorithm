def solution(n):
    answer = []

    def hanoi(n, start, destination, sub):
        if n == 1:
            answer.append([start, destination])
            return
        hanoi(n-1, start, sub, destination)
        answer.append([start, destination])
        hanoi(n-1, sub, destination, start)

    hanoi(n, 1, 3, 2)

    return answer
