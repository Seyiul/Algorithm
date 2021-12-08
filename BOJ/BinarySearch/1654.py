K, N = map(int, input().split())
lengths = []
for i in range(K):
    lengths .append(int(input()))

min_length = 1
max_length = max(lengths)
result = 0

while(min_length <= max_length):
    mean_length = (min_length + max_length) // 2

    cut_num = 0
    for length in lengths:
        cut_num += length // mean_length

    if(cut_num >= N):
        result = mean_length
        min_length = mean_length + 1

    elif(cut_num < N):
        max_length = mean_length - 1

print(result)
