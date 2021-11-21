from sys import stdin
line = stdin.readline()
result = 0

if '()' in line:
    line = line.replace('()', 'l')
while '(' in line:
    end = line.index(')')
    start = line[:end].rindex('(')
    n = line[start:end+1].count('l')
    result += n+1
    line = line[:start]+line[start+1:end]+line[end+1:]

print(result)
# ()(((()())(())()))(())
