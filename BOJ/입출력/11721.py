s = input()
for i in range(len(s)):
    if i % 10 == 0 and i != 0:
        print()
    print(s[i], end='')
