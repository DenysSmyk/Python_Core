def count_positives_sum_negatives(arr):
    res = []
    l = []
    s = []
    if arr == []:
        return []
    else:
        for i in arr:
            if i >0:
                l.append(i)
            elif i < 0:
                s.append(i)
        res.append(len(l))
        res.append(sum(s))
    return res