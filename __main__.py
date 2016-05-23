# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！

#jonathan's code

def list_of_pairs (number):
    a_list = []
    list_of_factors = List_prime_factors (number)
    for factor in list_of_factors:
        multiplicity = Find_Multiplicity (factor, number)
        a_list.append([ factor, multiplicity ])
    return a_list
print list_of_pairs(number)    
