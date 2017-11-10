def split(word, k):
    i = 0
    res = []
    tmp_res = ''
    idx = -1
    while i < len(word):
        if word[i] == ' ':
            if tmp_res!= '':
                res.append(tmp_res)
                tmp_res = ''
            i +=1
        else:
            if len(res)+1 == k:
                return i
            tmp_res += word[i]
            i+=1
    if tmp_res!= '' and word[-1]!= ' ':
        res.append(tmp_res)
    return idx
s = '   i am crystal'
print s[split(s, 4)]




