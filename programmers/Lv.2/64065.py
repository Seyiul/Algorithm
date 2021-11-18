def solution(s):
    nums = []
    s = list(s[2:-2].split('},{'))

    for i in s:
        i = list(map(int, i.split(',')))
        nums.append(i)

    dic = {num: 0 for num in max(nums, key=len)}
    print(dic)

    for i in nums:
        for d in dic:
            if d in i:
                dic[d] += 1
    print(dic)

    sorted_dic = sorted(dic.items(), reverse=True, key=lambda item: item[1])

    answer = []

    for key, value in sorted_dic:
        answer.append(key)

    return answer


'''
import re
def solution(s):

    answer = []
    a = s.split(',{')
    a.sort(key = len)
    for j in a:
        numbers = re.findall("\d+",j)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer

'''
