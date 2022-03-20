def solution(n):
    answer = 0

    for i in range(1, n+1):
        left, right = i, i + 1

        while left <= right:
            if sum(range(left, right)) == n:
                answer += 1
                break
            elif sum(range(left, right)) < n:
                right += 1
            elif sum(range(left, right)) > n:
                break

    return answer


print(solution(15))
