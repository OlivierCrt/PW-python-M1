from typing import Any


pa = [0,1,2,3,4,5]
pb = [0,2,3,4,5]

def addpoly(paParam,pbParam) :
    pres =[]
    temp =0
    maxlenght = max(len(paParam), len(pbParam))
    for i in range (maxlenght) :
        if len(paParam) == maxlenght :
            pres.append(paParam[i])
            temp = 0
        else :
            pres.append(pbParam[i])
            temp = 1
        print (pres)

    if temp == 1 :
        for i in range (len(paParam)) :
            pres[i] =(pres[i]+paParam[i])
    else :
        for i in range (len(pbParam)) :
            pres[i]=(pres[i]+pbParam[i])

    return pres

pad= {7:1}
pbd= {0:-6,1:5,2:3,5:1}
pcd= {0:1, 2000:1}


v1={1:10 , 7:4 , 8:9}
v2={1:5 , 7:2}




class Vecteur :
    def __init__(self,coeff):
        self.coeffs={}
        for (i,x) in enumerate(coeff) :
            if x!= 0.0:
                self.coeffs[i] = x

    def __repr__(self):
        return(repr(self.coeffs))


    def non_zero(self) :
        return set(self.coeffs.keys())
    
    def __getitem__(self,a) :
        return self.coeffs.get(a,0)
    
    def __setitem__(self,a,value) :
        if value!=0 :
            self.coeffs[a] = value

    
    def __add__(self,v2) :
        Nvecteur = Vecteur([])
        for a in (self.non_zero() | v2.non_zero()) :
            Nvecteur[a] =self[a] + v2[a]
        return  Nvecteur
    

v1 = Vecteur([1,2,3])
v2 = Vecteur([4,5,6])

vx = v1 + v2
print (vx)



class Complexe :
    def __init__(self, im , re):
        self.s_im = im
        self.s_re = re

    def __repr__(self):
        return "{real} + {imag} i".format(real=self.s_re, imag=self.s_im)
    
    
    def __add__(self,other) :
        ncomp = Complexe(0,0)
        ncomp.s_im = self.s_im + other.s_im
        ncomp.s_re = self.s_re + other.s_re
        return ncomp
    
    def __sub__(self,other) :
        ncomp = Complexe(0,0)
        ncomp.s_im = self.s_im - other.s_im 
        ncomp.s_re = self.s_re - other.s_re 
        return ncomp




c1 = Complexe(1,2)
c2 = Complexe(3,2)
print(c1)
c3 = c1+c2
c4 = c3 - c1
print(c3,c4)

        






