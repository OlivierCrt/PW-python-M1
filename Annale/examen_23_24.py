all_etudiants = ['superdupont', 'asterix', 'tyrion']
coeffs = [5,2,2]
notes_par_matière = [[15, 2, 5], [8, 5, 20], [19, 15, 13]]
matières = ["poterie","anglais","c++"]



def notes_par_etud(marks_list) :
    return marks_list

def make_dict(marks_list,names) :
    res=dict()
    for i in range (len(names)) :
        res[names[i]] =marks_list[i]

    return res
ds = make_dict(notes_par_matière,all_etudiants)
print(ds)

def moyenne(notes,liste_coef) :
    moy = 0
    sum_coef =0
    for i in range( len(notes)) :
        sum_coef=liste_coef[i] + sum_coef
        moy = moy + notes[i]*liste_coef[i]


    moy = moy/sum_coef
    return (moy)


moy = moyenne(notes_par_matière[0],coeffs)
print(moy)

def moyenne_dic(dictio) :
    res = dictio.copy()
    for i in (list(dictio.keys())) :
        res[i] = moyenne(dictio[i],[5,2,2])
    return (res)

print(moyenne_dic(ds))

def ajout_moyenne(dictio) :
    res = dictio.copy()
    for i in (list(dictio.keys())) :
        res[i].append(moyenne(dictio[i],[5,2,2]))

    return res
print(ajout_moyenne(ds))


def valide(dictio_note_moy):
    res=[]

    for key in (list(dictio_note_moy.keys())):
        size = len(dictio_note_moy[key])
        cpt=0
        moy_e=dictio_note_moy[key][size-1]
        for i in range(size-2) :
            note_mat=dictio_note_moy[key][i]
        
            if (note_mat>=6) :
                cpt+=1
            
        if (cpt>= size-2) and (moy_e >=10) :
            res.append(key)
    return res
print (valide(ds))






