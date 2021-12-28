n = int(input())
word = []

for _ in range(n):
    word.append(input())

word = list(set(word))
word.sort(key=lambda x: (len(x), x))

for w in word:
    print(w)
