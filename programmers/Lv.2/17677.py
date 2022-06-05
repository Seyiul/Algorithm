def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if str1 == str2:
        return 65536

    new_str1 = [str1[n:n+2]
                for n in range(0, len(str1)-1) if str1[n:n+2].isalpha()]
    new_str2 = [str2[n:n+2]
                for n in range(0, len(str2)-1) if str2[n:n+2].isalpha()]

    if len(new_str1) > len(new_str2):
        inter = len([new_str1.remove(x) for x in new_str2 if x in new_str1])
    else:
        inter = len([new_str2.remove(x) for x in new_str1 if x in new_str2])

    union = len(new_str1 + new_str2)

    return 65536 if union == 0 else int(inter/union * 65536)
