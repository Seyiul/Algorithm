s = list(input())

num = 0
digit = []
for i in s:
    if i.isalpha():
        digit.append(i)
    else:
        num += int(i)
digit.sort()
print(''.join(digit) + str(num))
