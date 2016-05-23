# -*- coding: utf-8 -*-
#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

''' DEEVY'S FUNCTION: compare_factors(list1, list2)'''
def compare_factors(list1, list2):
    length_1 = len(list1)
    length_2 = len(list2)

    list_1_factors = []
    list_2_factors = []

    factors_length_1 = len(list_1_factors)
    factors_length_2 = len(list_2_factors)

    longer_factors_list = list_1_factors
    shorter_factors_list = list_2_factors

    overlap = []  # A map of where the first number of the pair matches between the two lists

    final_value = 0  # Number of common numbers

    if factors_length_1 > factors_length_2:  # Finds list with more factors
        longer_factors_list = list_1_factors
        shorter_factors_list = list_2_factors
    elif factors_length_2 > factors_length_1:
        longer_factors_list = list_2_factors
        shorter_factors_list = list_1_factors
    else:
        longer_list = list_1_factors
        shorter_list = list_2_factors

    for x in range(length_1):  # Puts the first number in list1 in a list
        list_1_factors.append(list1[x][0])
        x += 1

    for x in range(length_2):  # Puts the first number in list2 in a list
        list_2_factors.append(list2[x][0])
        x += 1

    for x in range(
            len(shorter_factors_list)):  # If the first number in each tuple is the same in both lists, write true
        flag = False  # Evaluate false after loop
        for y in range(len(longer_factors_list)):
            if shorter_list[x] == longer_list[y]:  # Compares numbers
                overlap.append(y)
                flag = True
        if flag == False:
            overlap.append("no")  # Can't use 'False' or '0' because they are used interchangeably in python

    for index in range(len(overlap)):  # Finds how many times there is a common number between the lists
        if overlap[index] != "no":
            if list1[index][1] < list2[overlap[index]][1]:  # Looks at where overlap points in the second list
                final_value += list1[index][1]
            else:
                final_value += list2[overlap[index]][1]

    total_nums = 0
    for pair in list1:  # Finds the total number of numbers
        total_nums += pair[1]
    for pair in list2:
        total_nums += pair[1]

    output = float(final_value) / float(
        total_nums)  # Divides the number of common numbers by the total number of numbers
    output = round(output, 2)

    print output
    return output
=======
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
>>>>>>> e5bdb19415399a995d63bacf0609c3b2d12e4da7

#JG Changes
def list_of_pairs (number):
    a_list = []
    list_of_factors = List_prime_factors (number)
    for factor in list_of_factors:
        multiplicity = Find_Multiplicity (factor, number)
        a_list.append([ factor, multiplicity ])
    return a_list
print list_of_pairs(number)    
=======
#Alec Battisti Multiplicity Function
def multiplicity(f,n):
    mult = 0
    while n%f == 0:
        mult+=1
        n = n/f
    print "Multiplicity: "+str(mult)
    return mult
    
>>>>>>> 6d84022b67553bd52f298ea7891b0fd5625dd54c
=======
#luke's code:
percent = 5
n = 0
def sentence_spitter(n):
    
    message_0 = "error: less than 0"

    message0 = "No match detected whatsoever. If you're already dating, it may be in your best interest to end your relationship immediately as there is no chance it will work out (sorry, man)."
    message1 = "A very slight match was detected. There is a small chance that this relationship will work out but it's probably more worth both of your time to find a new mate."
    message2 = "This low of a score indicates that both parties should perform a detailed analysis of the relationship in question."
    message3 = "A slight match was detected. If you're not prepared to put your whole heart and soul into this relationship, it might be time to give up."
    message4 = "A moderate match has been detected. Hard work and dedication will help your relationship thrive and potentially grow into something great. A few minor slip ups, however, may cause the relationship to fall apart completely; stay cautious."
    message5 = "There is a good chance that it could work out, but you should still be careful because anything negative could mess up your chances."
    message6 = "Things are looking positive for you two. This could work..."
    message7 = "You have good reason to feel optimistic. Your chances may be better than you were expecting."
    message8 = "Stay positive and everything will be fine... if you're lucky."
    message9 = "The chances are good that you could make this work. The whole period 5 CSE team is rooting for you."
    message10 = "Almost a 50% match! Your odds are very favorable."
    message11 = "I can feel the sparks flying from here! This type of connection is quite rare, do not take it for granted."
    message12 = "The connection between you two is potentially something to brag about. There is a very good chance that it could work."
    message13 = "The connection that you share with this person is one that could make other couples jealous. Be careful who you flaunt towards."
    message14 = "The level of intimacy that is shared by you could go down in history as one of the greatest romances of all time."
    message15 = "A match of this caliber could potentially be considered 'true love'."
    message16 = "A match of this caliber could definitely be considered 'true love'."
    message17 = "Was it really even necessary for you to use this program? It should already be obvious to both of you that you were meant to be."
    message18 = "Wow! Your connection is one of great significance! Not much work will be required to perfect your relationship."
    message19 = "This kind of match is quite unique. Treat each other well from here on out for perfect results."
    message20 = "An almost completely perfect match! Whatever you're doing, it's working, and if you're not already together, it's time to make your move."
    message21 = "A perfect match! Honestly you two should already be married, unless of course you just entered your own name twice, in which case, you're very lonely."
    
    percent = str(int(n * 100))
    
    if n < 0:
        return message_0
    if n == 0:
	return percent + "% match-- " + message0
    if .01 < n <= 0.05:
	return percent + "% match -- " + message1
    if .05 < n <= 0.10:
	return percent + "% match -- " + message2
    if .10 < n <= 0.15:
	return percent + "% match -- " + message3
    if .15 < n <= 0.20:
	return percent + "% match -- " + message4
    if .20 < n <= 0.25:
	return percent + "% match -- " + message5
    if .25 < n <= 0.30:
	return percent + "% match -- " + message6
    if .30 < n <= 0.35:
	return percent + "% match -- " + message7
    if .35 < n <= 0.40:
	return percent + "% match -- " + message8
    if .40 < n <= 0.45:
	return percent + "% match -- " + message9
    if .45 < n <= 0.50:
	return percent + "% match -- " + message10
    if .50 < n <= 0.55:
	return percent + "% match -- " + message11
    if .55 < n <= 0.60:
	return percent + "% match -- " + message12
    if .60 < n <= 0.65:
        return percent + "% match -- " + message13
    if .65 < n <= 0.70:
	return percent + "% match! -- " + message14
    if .70 < n <= 0.75:
	return percent + "% match! -- " + message15
    if .75 < n <= 0.80:
	return percent + "% match! -- " + message16
    if .80 < n <= 0.85:
	return percent + "% match! -- " + message17
    if .85 < n <= 0.90:
	return percent + "% match! -- " + message18
    if .90 < n <= 0.95:
	return percent + "% match! -- " + message19
    if .95 < n <= .990:
	return percent + "% match!! -- " + message20
    if n == 1.0:
	return percent + "%!!! -- " + message21
    
print sentence_spitter(1)
>>>>>>> 8008034963620741b3f18fe559eb7445c7c222f6
