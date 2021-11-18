def convert(n,base):
    T = '0123456789ABCDEF'
    q,r = divmod(n,base)
    if q == 0:
        return T[r]
    else:
        return convert(q,base) + T[r]
def solution(n, t, m, p):
    arr = []
    for i in range(t*m):
        num = convert(i,n)
        for j in range(len(num)):
            arr.append(num[j])
    
    answer = [arr[s] for s in range(len(arr)) if s%m==(p-1)]
    return ''.join(answer[:t])