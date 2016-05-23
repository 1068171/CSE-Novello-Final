# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！


# Abirami
def list_prime_factors(num):
    n = int(num)
    prime = []
    for x in range (2,n+1):
        pr = True
        for i in range (2,x):
            if (x%i==0):
                pr = False  
        if pr:
            if n%x==0:
                prime.append(x)
    print prime
    return prime