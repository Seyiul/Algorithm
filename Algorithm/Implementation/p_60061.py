def solution(n, build_frame):
    answer = []

    def check_rules(answer):
        for x, y, stuff in answer:
            if stuff == 0:
                if y == 0 or [x, y-1, 0] in answer or ([x-1, y, 1] in answer or [x, y, 1] in answer):
                    continue
                return False

            elif stuff == 1:
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                return False
        return True

    for f in build_frame:
        x, y, a, b = f[0], f[1], f[2], f[3]

        if b == 0:
            answer.remove([x, y, a])
            if not check_rules(answer):
                answer.append([x, y, a])

        if b == 1:
            answer.append([x, y, a])
            if not check_rules(answer):
                answer.remove([x, y, a])

    return sorted(answer)


print(solution(5, 	[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
