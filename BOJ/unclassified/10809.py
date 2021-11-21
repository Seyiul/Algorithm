s = input()
alpha = [-1] * 26
for i in s:
    alpha[ord(i) - ord('a')] = s.index(i)

print(' '.join(str(a) for a in alpha))
