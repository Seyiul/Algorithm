import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

max_team = n//2 if m >= n//2 else m
n -= max_team * 2
m -= max_team
k = k - n - m

while k > 0:
    max_team -= 1
    k -= 3

print(max_team)
