
# def solution(numbers):
#     answer = ''
#     zero = []
#     numbers = list(map(str,numbers))
#     for n in numbers:
#         if('0' in n):
#             zero.append(n)
#             numbers.remove(n)
#     numbers.sort(key = lambda x : (x[0],int(x)), reverse = True)
#     numbers = ''.join(numbers)

#     zero.sort()
#     zero = ''.join(zero)

#     answer = numbers+zero
#     return answer

from itertools import permutations


def solution(numbers):
    answer = ''

    num = list(permutations(numbers, len(numbers)))

    max = 0
    for n in num:
        n = map(str, n)
        n = int(''.join(n))
        if n > max:
            max = n

    return str(max)


print(solution([6, 10, 2]))
