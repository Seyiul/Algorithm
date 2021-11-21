s = input()
alpha = [0] * 26
for i in s:
    alpha[ord(i) - ord('a')] += 1

print(' '.join(str(a) for a in alpha))
