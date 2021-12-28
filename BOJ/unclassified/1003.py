t = int(input())

zero = [1, 0]
one = [0, 1]


def cal(n):
    for i in range(len(zero), n+1):
        zero.append(zero[i-2] + zero[i-1])
        one.append(one[i-2] + one[i-1])

    print(zero[n], one[n])


for _ in range(t):
    n = int(input())
    cal(n)
