def solution(n, arr1, arr2):
    answer = []
    for map1 in range(len(arr1)):
        arr1[map1] = format(arr1[map1],'b')
        arr1[map1] = list(map(int,str(arr1[map1]).zfill(n)))
    
    for map2 in range(len(arr2)):
        arr2[map2] = format(arr2[map2],'b')
        arr2[map2] = list(map(int,str(arr2[map2]).zfill(n)))
        
    for i in range(n):
        line = ''
        for j in range(n):
            if arr1[i][j] == 1 or arr2[i][j] == 1:
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer