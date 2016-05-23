# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！

#Alec Battisti Multiplicity Function
def multiplicity(f,n):
    mult = 0
    while n%f == 0:
        mult+=1
        n = n/f
    print "Multiplicity: "+str(mult)
    return mult
    