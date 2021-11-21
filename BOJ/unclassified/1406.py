from sys import stdin
st1 = list(stdin.readline().strip())
st2 = []
n = int(input())
cursor = len(st1)

for i in range(n):
    order = stdin.readline().split()

    if order[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif order[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif order[0] == 'B':
        if st1:
            st1.pop()
    elif order[0] == 'P':
        st1.append(order[1])

print(''.join(st1+st2[::-1]))
