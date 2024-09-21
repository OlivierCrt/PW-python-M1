#tp1 10/09/2024 Crampete Olivier

import urllib.request

t = urllib.request.urlopen("https://www.irit.fr/~Philippe.Muller/alice_wonderland.utf8.txt")
text = t.read().decode('utf-8')


#text not pretreated
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



#Pretreated text 21/09
ttr = urllib.request.urlopen("https://www.irit.fr/~Philippe.Muller/alice_wonderland.utf8.conll")
text_pretreated = ttr.read().decode('utf-8')

def create_dict(text_pretreated) :
    lines_list = text_pretreated.split("\n")
    res = dict()
    for i in range (len(lines_list)) :
        lines_list[i] = lines_list[i].split("\t")
        if len(lines_list[i]) >= 2:
            if lines_list[i][1] in res :
                res[lines_list[i][1]].append(lines_list[i][0])

            else :
                res[lines_list[i][1]] = [lines_list[i][0]]      
    return res

def wordCount_Categorie(categorie , dictio) :
    if categorie in dictio :
        return (len(dictio[categorie]))
    else :
        return 0
    
def wordCount_Word(word , dictio) :
    i=0
    for cat,words in dictio.items() :
        for w in  words:
            if w == word :
                i= i+1
    return i

def max_word_Categorie(categorie,dictio) :
    if categorie not in dictio :
        return None 
    
    wordCount_dict = dict()#{word : value... }

    for word in dictio[categorie] :
        if word in wordCount_dict :
            wordCount_dict[word]+=1
        else :
            wordCount_dict[word] = 1

    #max
    max_word =''
    max_value =0

    for word,i in wordCount_dict.items() :
        if i > max_value :
            max_value = i
            max_word=word
    return max_word,max_value

#Sequences n-gram

#1) Not pretreated text
def n_gram_list_create(n , text_p) :
    dict_res=dict()# {word(0) : [next word(1) , next word(n)}
    text_temp = text_p
    for ch in [',','.',';','!','?',':',"'",'-','(',')','/','*','[',']'] :
        if ch in text_temp :
            text_temp =text_temp.replace(ch," ")

    text_temp = text_temp.lower()
    text_temp = text_temp.split() 
    for i in range (len(text_temp)-n+1) :

        if text_temp[i] not in dict_res :
            dict_res[text_temp[i]]=text_temp[i+1:i+n]
            
        else:
           dict_res[text_temp[i]].append(text_temp[i+1:i+n])

    return dict_res


print(n_gram_list_create(3,text))


    
    









#Test pretreated text
'''d =create_dict(text_pretreated)
print("Max word in categorie PP :")
print(max_word_Categorie('PP',d))
print("Number of occurences of 'Alice':")
print(wordCount_Word('Alice',d))
print("Words for NP categorie: ")
print(wordCount_Categorie('NP',d))'''


