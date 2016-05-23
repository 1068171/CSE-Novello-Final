# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！



'''ACHYUTH'S FUNCTION: parse_to_number(input)'''

def alpha_numeric_dictionary(a):
#Lowercase   
    if a == 'a':
        return 1
    if a == 'b':
        return 2
    if a == 'c':
        return 3
    if a == 'd':
        return 4
    if a == 'e':
        return 5
    if a == 'f':
        return 6
    if a == 'g':
        return 7
    if a == 'h':
        return 8
    if a == 'i':
        return 9
    if a == 'j':
        return 10
    if a == 'k':
        return 11
    if a == 'l':
        return 12
    if a == 'm':
        return 13
    if a == 'n':
        return 14
    if a == 'o':
        return 15
    if a == 'p':
        return 16
    if a == 'q':
        return 17
    if a == 'r':
        return 18
    if a == 's':
        return 19
    if a == 't':
        return 20
    if a == 'u':
        return 21
    if a == 'v':
        return 22
    if a == 'w':
        return 23
    if a == 'x':
        return 24
    if a == 'y':
        return 25
    if a == 'z':
        return 26
#Caps       
    if a == 'A':
        return 1
    if a == 'B':
        return 2
    if a == 'C':
        return 3
    if a == 'D':
        return 4
    if a == 'E':
        return 5
    if a == 'F':
        return 6
    if a == 'G':
        return 7
    if a == 'H':
        return 8
    if a == 'I':
        return 9
    if a == 'J':
        return 10
    if a == 'K':
        return 11
    if a == 'L':
        return 12
    if a == 'M':
        return 13
    if a == 'N':
        return 14
    if a == 'O':
        return 15
    if a == 'P':
        return 16
    if a == 'Q':
        return 17
    if a == 'R':
        return 18
    if a == 'S':
        return 19
    if a == 'T':
        return 20
    if a == 'U':
        return 21
    if a == 'V':
        return 22
    if a == 'W':
        return 23
    if a == 'X':
        return 24
    if a == 'Y':
        return 25
    if a == 'Z':
        return 26

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