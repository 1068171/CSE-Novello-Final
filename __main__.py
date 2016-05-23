#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！


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