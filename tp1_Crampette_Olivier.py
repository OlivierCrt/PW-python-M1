#tp1 10/09/2024 Crampete Olivier

import urllib.request

t = urllib.request.urlopen("https://www.irit.fr/~Philippe.Muller/alice_wonderland.utf8.txt")
text = t.read().decode('utf-8')



def wordCount(text_p) :
    res=0
    resdict={}
    text_temp = text_p
    for ch in [',','.',';','!','?',':',"'",'-','(',')','/','*'] :
        if ch in text_temp :
            text_temp =text_temp.replace(ch," ")

    text_temp = text_temp.lower()
    text_temp = text_temp.split()  

    for i in text_temp :
        if i in resdict :
            resdict[i] +=1

        else :
            resdict[i] = 1
    return resdict

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

def top10values(dict_p) :
    dp_sorted =sorted(dict_p.items(), key=lambda t: t[1] , reverse=True)
    for i in dict_p :
        d = dp_sorted[:10]

    return d


ttr = urllib.request.urlopen("https://www.irit.fr/~Philippe.Muller/alice_wonderland.utf8.conll")
text_pretreated = ttr.read().decode('utf-8')


lines = text_pretreated.split("\n")
print (lines)



'''
dictio= wordCount(text)
print( maxValueInDict(dictio) )
print( top10values(dictio))
'''


