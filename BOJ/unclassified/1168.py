from sys import stdin
from collections import deque

a, b = map(int, (stdin.readline().split()))
deq = deque([i for i in range(1, a+1)])
i = 0
ans = []
while len(deq):
    deq.rotate(-b+1)
    ans.append(str(deq.popleft()))

print('<', ', '.join(ans), '>', sep='')
