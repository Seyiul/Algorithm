import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    books = [False] * (n+1)
    student = []

    for _ in range(m):
        student.append(list(map(int, input().split())))

    student.sort(key=lambda x: x[1])

    ans = []
    for s in student:
        if len(ans) == 0:
            ans.append(s)
            books[s[0]] = True
        elif ans[-1][1] <= s[1]:
            for i in range(s[0], s[1]+1):
                if books[i] == False:
                    ans.append(s)
                    books[i] = True
                    break

    print(len(ans))
