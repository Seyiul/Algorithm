from itertools import combinations


def solution(clothes):
    dict = {}
    for cloth, c_type in clothes:
        if c_type in dict:
            dict[c_type] += 1
        else:
            dict[c_type] = 1

    ans = 1
    for d in dict.values():
        ans *= d+1
    return ans - 1
