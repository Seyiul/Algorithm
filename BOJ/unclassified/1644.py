n = int(input())

prime_list = [False, False] + [True]*(n-1)

for i in range(int(n**0.5)+1):
    if prime_list[i]:
        for j in range(i+i, n+1, i):
            prime_list[j] = False

prime_list = [num for num in range(2, n+1) if prime_list[num] == True]

cnt = 0

start = 0
end = 0

while end <= len(prime_list):
    tmp_sum = sum(prime_list[start:end])

    if tmp_sum == n:
        cnt += 1
        end += 1
    elif tmp_sum < n:
        end += 1
    else:
        start += 1

print(cnt)
