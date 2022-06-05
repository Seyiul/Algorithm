from itertools import combinations


def solution(orders, course):
    answer = []
    for k in course:
        candidates = {}
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                if res in candidates:
                    candidates[res] += 1
                else:
                    candidates[res] = 1

        answer += [menu for menu, cnt in candidates.items() if cnt >
                   1 and cnt == max(candidates.values())]
    return sorted(answer)
