# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！


# Abirami
import math

def list_prime_factors(num):
    n = int(num)
    prime = []
    k=1
    if n%2==0:
        prime.append(2)
        
    flag = 0
    while (2*k+2)**2 < n:
        if n%(2*k+1)==0:
            for p in prime:
                if (2*k+1)%p ==0:
                    flag = 1
            if flag ==+ 0:
                prime.append(2*k+1)
        flag = 0
        k=k+1
    if len(prime)== 0:
        prime.append(n)
        
    print prime
    return prime