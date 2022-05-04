def solution(id_list, report, k):
    report_list = {i: [] for i in id_list}
    report_num = {i: 0 for i in id_list}

    for r in report:
        a, b = r.split()[0], r.split()[1]
        if a in report_list and b not in report_list[a]:
            report_list[a].append(b)
            report_num[b] += 1

    banned = [i for i, j in report_num.items() if j >= k]

    answer = []
    for i, j in report_list.items():
        cnt = 0
        for b in banned:
            if b in j:
                cnt += 1
        answer.append(cnt)

    return answer
