# <-- it's the sign to make comments in python

# with three sign double quote (") or single quote (') we us make multiline comments also
"""
It's an example about
multiline comments
now star with the other things of python
"""

'''
it also is a multipleline
comment
now let's go to star with variables in python
'''

# print is use for show by console something that we want to showing
print("Hello world")
# print can show sum, subtrations, multiplication, divition, numbers, text, variables and other king of data saving
print(-3 + 8)
print(55 - 66)
print(5 * 2)
print(5 / 2)

# additionaly we can give a value with text and concatenate with another value to print
print("Here are the value of sum: ", 5 + 5)

################################## variables #######################################
'''
The variables in python aren't strongly typed, this can save all king of data like strings,
integers, floats, objects, etc.
'''
# for declarate variables we have to give a name to a variable and have two options: <name variable> | = <value to save> |
# first initialise the variable
fullName = "Juan Olaya"
print(fullName)
# second not initialise the variable, and initialise after in the program
sum
print(sum)
sum = 5 + 5
print(sum)

# also can change the type of data saving inside of variable
sum = "No fun"
print(sum)

################################## input #######################################
'''
In python when you want to get a value but is the user whom give the value, 
we can catch it value inside a variable,
but to catch the value we use the key word "input",
this function show text to console and wait to the user insert the information or data 
that I need for our program
'''

name = input("What is your name? ")
print("Hi!, " + name + " nice too meet you.")