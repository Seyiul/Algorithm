def solution(dartResult):
    score = []
    shoot = ''
    for dart in list(dartResult):
        if dart.isdigit():
            shoot += dart
        else:
            if len(shoot) != 0:
                score.append(shoot)
                shoot = ''
            if dart == 'D':
                score[-1] = int(score[-1])**2
            elif dart == 'T':
                score[-1] = int(score[-1])**3
            elif dart == '*':
                if len(score) > 1:
                    score[-2] = int(score[-2])*2
                score[-1] = int(score[-1])*2
            elif dart == '#':
                score[-1] = int(score[-1])*(-1)
    return sum(map(int,score))