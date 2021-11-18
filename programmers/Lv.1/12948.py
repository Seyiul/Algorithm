def solution(phone_number):
    phone_number = ''.join(list(map(lambda x : x.replace(x,'*'),phone_number[:-4])) + list(phone_number)[-4:])
    return phone_number