def parse_to_number(achyuth):
    final = 0
    letters = []
    numbers = []
    for i in achyuth:
        letters.append(i[0])
        numbers.append(i[1] - 1)


    
    
    
    for i in range(0, len(letters)):
        numero = alpha_numeric_dictionary(letters[i])
        final = final + (numero * (26**(numbers[i]%9)))
    return final

