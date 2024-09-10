#tp1 10/09/2024 Crampete Olivier

import urllib.request

t = urllib.request.urlopen("https://www.irit.fr/~Philippe.Muller/alice_wonderland.utf8.txt")
text = t.read().decode('utf-8')



def wordCount(text_p,word) :
    text_temp = text_p

    for ch in [',','.',';','!','?',':',"'"] :
        if ch in text_temp :
            text_temp =text_temp.replace(ch," ")

    print(text_temp)
    text_temp = text_temp.split()
    res=0
    for i in text_temp :
        if i == word :
            res=res+1 
    return res

print (wordCount(text , "However"))



