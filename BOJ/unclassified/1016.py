min, max = map(int, input().split())

num = set(range(min, max+1))

for i in range(2, int(max**0.5)+1):
    square = i**2
    num -= set(range((min//square)*square, max+1, square))

print(len(num))
