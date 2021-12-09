import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

count = Counter(card)

for i in range(len(arr)):
    if arr[i] in count:
        print(count[arr[i]], end=' ')
    else:
        print(0, end=' ')

# def find(i, start, end):
#     while start <= end:
#         mid = (start+end)//2
#         if card_set[mid] == i:
#             return card.count(i)
#         elif card_set[mid] < i:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0


# start, end = 0, len(card_set)-1
# for i in arr:
#     print(find(i, start, end), end=' ')
