##################################################################
#  Student name: Leila Yammine
#  Course: COSC 4603 - Computer Theory
#  Assignment: #0 - Regular Expression Character Checker
#  File name: Yammine0.py
#  Program Purpose: Checks user input of a maximum of 1,000 characters and validates as a regular expression if it contains only the characters {0,1,+,*,(,)} 
#
#  Program Limitations: None known
#  Development Computer: Macbook Pro
#  Operating System: OS X Mavericks
#  Integrated Development Environment (IDE): None (Terminal)
#  Program's Operational Status: Works perfectly
##################################################################

import sys

def main():
    while True:
        expression = str(raw_input("Enter a regular expression: "))
        if len(expression) > 1000:
            print "\nCannot enter more than 1,000 characters. Try again.\n"
            continue
        expression = removeSpaces(expression)
        isValidRegExpression = False
        for char in expression:
            if isValid(char):
                isValidRegExpression = True
            else:
                isValidRegExpression = False
                break

        printResult(expression, isValidRegExpression)
        if isValidRegExpression == False:
            break
# End main()

# Checks if given character belongs to the set of acceptable input characters
def isValid(char):

    if char == '(':
        return True
    elif char == ')':
        return True
    elif char == '0':
        return True
    elif char == '1':
        return True
    elif char == '+':
        return True
    elif char == '*':
        return True
    else:
        return False

# Prints a new line with a '^' directly beneath any invalid characters
def markInvalidChars(expression):
    errormarker = "           "
    for char in expression:
        if isValid(char):
            errormarker += " "
        else:
            errormarker += "^"
    print errormarker

# Prints the result
def printResult(expression, isValidRegExpression):
    if isValidRegExpression == True:
        print "VALID:  ", expression
    else:
        print "INVALID:  ", expression
        markInvalidChars(expression)
        print "\nProgram terminated"

# Removes any whitespace from raw user input
def removeSpaces(expression):
    truncExpression = ""
    for char in expression:        
        if char != " " and char != "\t":
            truncExpression += char
    return truncExpression

if __name__ == '__main__':
    main()
