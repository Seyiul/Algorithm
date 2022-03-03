def solution(genres, plays):
    ans = []
    sum_dict = {}
    dict = {}
    for i in range(len(genres)):
        if genres[i] in sum_dict:
            sum_dict[genres[i]] += plays[i]
            dict[genres[i]].append([i, plays[i]])
        else:
            sum_dict[genres[i]] = plays[i]
            dict[genres[i]] = []
            dict[genres[i]].append([i, plays[i]])

    sum_sdict = sorted(sum_dict.items(), key=lambda x: x[1], reverse=True)
    for key, val in sum_sdict:
        sdict = sorted(dict[key], key=lambda x: x[1], reverse=True)
        for song in sdict[:2]:
            ans.append(song[0])

    return ans
