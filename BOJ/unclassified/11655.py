from sys import stdin
s = stdin.readline().rstrip('\n')
answer = ''
for i in s:
    if i.islower():
        if ord(i) + 13 > ord('z'):
            answer += chr(ord(i)-13)
        else:
            answer += chr(ord(i)+13)
    elif i.isupper():
        if ord(i) + 13 > ord('Z'):
            answer += chr(ord(i)-13)
        else:
            answer += chr(ord(i)+13)
    else:
        answer += i

print(answer)
