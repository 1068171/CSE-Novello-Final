# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！

'''ACHYUTH'S FUNCTION: parse_to_number(input)'''

def parse_to_number(achyuth):

#defining variables    
    final = 0
    letters = []
    numbers = []
    
#splits the input into two lists by first and second value    
    for i in achyuth:
        letters.append(i[0])
        numbers.append(i[1] - 1)

#takes input from alpha-numeric dictionary and numbers, then adds the numbers up
    for i in range(0, len(letters)):
        numero = alpha_numeric_dictionary(letters[i])
        final = final + (numero * (26**(numbers[i]%9)))

#returns and prints  
    return final
    print final