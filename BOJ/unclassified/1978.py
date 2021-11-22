import math


def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in range(n):
    if is_prime_num(nums[i]):
        ans += 1
print(ans)
