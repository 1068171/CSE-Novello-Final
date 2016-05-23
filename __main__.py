#Before you push your additions to the code, make sure they exactly fit the parameters described in the project!
#Let's write delicious code. がんばってくらさい！
print "Enter in loveTest in the commandline followed by the two names in parentheses with commas in between"
def loveTest(name1, name2)
    number1 = name_to_number(name1)
    number2 = name_to_number(name2)
    try:
        number1 = int(number1)
        number2 = int(number2)
    except:
        print("Error with name_to_number function. Attempted to make the output of the function into an integer but failed")
    factor1 = factor(number1)
    factor2 = factor(number2)
    try:
        comparedFactor1 = compare_factor(factor1, factor2)
    except:
        print("Error in comparedFactor1 function")
    InterestingResponse1 = InterestingResponseFunction(comparedFactor1)
    print InterestingResponse1

