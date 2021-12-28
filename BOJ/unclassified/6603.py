import itertools

arr = list(map(int, input().split()))

while len(arr) != 1 and arr[0] != 0:
    k = arr[0]
    arr = arr[1:]

    answer = []

    def dfs(idx, list):
        if len(list) == 6:
            answer.append(list[:])
            return

        for i in range(idx, k):
            dfs(i+1, list+[arr[i]])

    dfs(0, [])

    for i in answer:
        for j in i:
            print(j, end=' ')
        print()

    print()
    arr = list(map(int, input().split()))
