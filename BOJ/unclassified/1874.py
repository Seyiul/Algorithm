n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
ans = []
idx = 0
i = 1

while idx < n:
    if len(stack) > 0 and stack[-1] == arr[idx]:
        ans.append('-')
        idx += 1
        stack.pop()
    else:
        ans.append('+')
        if(i > n):
            print('NO')
            break
        else:
            stack.append(i)
            i += 1
else:
    for a in ans:
        print(a)
