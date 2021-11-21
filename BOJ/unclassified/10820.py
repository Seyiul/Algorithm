from sys import stdin
while 1:
    s = stdin.readline().rstrip('\n')
    if not s:
        break
    blank = 0
    low = 0
    cap = 0
    digit = 0
    for i in s:
        if i == ' ':
            blank += 1
        if i.isdigit():
            digit += 1
        if i.islower():
            low += 1
        if i.isupper():
            cap += 1
    print(low, cap, digit, blank)
