from itertools import permutations


def solution(expression):
    ops = set()
    exp = []
    num = ''

    for i in expression:
        if not i.isdigit():
            exp.append(num)
            num = ''
            exp.append(i)
            ops.add(i)
        else:
            num += i
    if num != '':
        exp.append(num)

    priority_list = list(permutations(ops, len(ops)))
    max_val = 0

    for priority in priority_list:
        new_exp = exp
        for op in priority:
            while op in new_exp:
                idx = new_exp.index(op)
                res = eval(''.join(new_exp[idx-1:idx+2]))
                new_exp = new_exp[:idx-1] + [str(res)] + new_exp[idx+2:]

        max_val = max(max_val, abs(int(new_exp[0])))

    return max_val


print(solution("50*6-3*2"))
print(solution("100-200*300-500+20"))
