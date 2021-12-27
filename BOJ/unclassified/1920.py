n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
arr = list(map(int, input().split()))


def find(i, start, end):
    while start <= end:
        mid = (start+end)//2
        if num[mid] == i:
            return True
        elif num[mid] < i:
            start = mid+1
        else:
            end = mid-1
    return False


start, end = 0, n-1

for i in arr:
    if find(i, start, end) == True:
        print(1)
    else:
        print(0)
