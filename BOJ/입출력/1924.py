days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

a, b = map(int, input().split())
n = 0

for i in range(1, a):
    if i == 4 or i == 6 or i == 9 or i == 11:
        n += 30
    elif i == 2:
        n += 28
    else:
        n += 31

n += b-1

print(days[n % 7])
