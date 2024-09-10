def maxValueInDict(dict_p):
    if not dict_p : 
        return None,None
    res= 0
    for i in dict_p.values() :
        if i > res :
            res = i

    for j in dict_p.keys() :
        if dict_p[j] == res :
            res_j = j
            break

    return j,res