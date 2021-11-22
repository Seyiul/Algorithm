def convert_D(n, base):
    num = 0
    base = int(base)
    for idx, i in enumerate(n):
        num += int(i) * (base**(len(n)-idx-1))
    return num


def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return r
    else:
        return convert(q, base) + r


a, b = map(int, input().split())
n = int(input())
nums = input().split()
ans = []
for i in range(n):
    num = convert_D(nums[i], a)
    num = convert(num, b)
    ans.append(int(num))

print(ans)
