n = int(input())
arr = list(map(int, input().split()))

m = int(input())
ask = list(map(int, input().split()))

for i in range(m):
    if ask[i] in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')
