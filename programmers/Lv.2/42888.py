def solution(record):
    answer = []
    dic = {}

    for r in record:
        chat = list(r.split(" "))
        if chat[0] == 'Enter' or chat[0] == 'Change':
            dic[chat[1]] = chat[2]

    for r in record:
        chat = list(r.split(" "))
        if chat[0] == 'Enter':
            answer.append(dic[chat[1]]+'님이 들어왔습니다.')
        elif chat[0] == 'Leave':
            answer.append(dic[chat[1]]+'님이 나갔습니다.')

    return answer
