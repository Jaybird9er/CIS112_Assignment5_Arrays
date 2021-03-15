""" 
Author: Jamey Kirk
Title: Assignment5_Lists
Date: 03/14/2021
Description: tests the function main and other array functions 
"""

# functions

def setZero(zeroList):
    """
    initializes any one-dimensional list to 0 
    """
    xList = [0 for x in range(20)]
    aList = xList.copy()
    return aList

def inputArray (userArr):
    """
    prompts user to input 20 integers
    """
    userInput = 0
    print("Enter 20 integers:")
    while userInput < len(userArr):
        userArr[userInput] = int(input())
        userInput += 1
    return userArr

def doubleArray (baseList, dubList):
    """
    initializes the elements of beta to two times the corresponding elements in alpha
    """
    for item in range(len(baseList)):
        dubList[item] = baseList[item] * 2
    return dubList

def copyGamma (stockList, gammaList):
    """
    sets the elements of the first row of inStock from gamma and the remaining rows 
    of inStock to three times the previous row of inStock
    """
    print("", end="\n\n")
    print("inStock after a call to copyGamma:")
    for row in range(len(stockList)):
        col = 0
        while col < len(gammaList):
            if row == 0:
                stockList[row][col] = gammaList[col]
            else:
                stockList[row][col] = gammaList[col] * pow(3, row) 
            print(stockList[row][col], end="\t")
            col += 1
        print("")

def copyAlphaBeta (aList, bList, inList):
    """
    stores alpha into the first five rows of inStock and beta into the last 
    five rows of inStock
    """
    print("", end="\n\n")
    print("inStock after a call to copyAlphaBeta:")
    row = 0
    while row < len(inList) / 2:
        col = 0
        while col < len(inList[0]):
            inList[row][col] = aList[col + (row * 4)]
            inList[row + 5][col] = bList[col + (row * 4)]
            col += 1
        row += 1
    row = 0
    while row < len(inList):
        col = 0
        while col < len(inList[0]):
            if ((col + 1) % 4 == 0):
                print(inList[row][col], end="\t")
                print("", end="\n")
            else:
                print(inList[row][col], end="\t")
            col += 1
        row += 1

def printArray (oneDList):
    """
    prints any one-dimensional list
    """
    count = 0
    for item in oneDList:
        if count == len(oneDList) / 2:
            print("", end="\n")
            print(item, end="\t")
        else:
            print(item, end="\t")
        count += 1

def setInStock (dList, inList):
    """
    after the user inputs elements for first column of inStock
    it sets elements in remaining columns to 2x the corresponding 
    element of previous column - corresponding delta(list) element
    """
    userArr = [0 for x in range(10)]
    userInput = 0
    print("Enter 10 integers:")
    while userInput < len(userArr):
        userArr[userInput] = int(input())
        userInput += 1
    print("", end="\n\n")
    print("inStock after a call to setInStock:")
    row = 0
    while row < len(inList):
        col = 0
        while col < len(inList[0]):
            if col == 0:
                inList[row][col] = userArr[row]
            else:
                inList[row][col] = inList[row][col - 1] * 2 - delta[row]
            print(inList[row][col], end="\t")
            col += 1
        print("")
        row += 1

# variables and objects

inStock = [[None for x in range(4)] for y in range(10)]
alpha = [None for x in range(20)]
beta = [None for x in range(20)]
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

# main program

print("Alpha after initialization:")
alpha = setZero(alpha)
printArray(alpha)
print("\n\n")
alpha = inputArray(alpha)
print("\n")
print("Alpha after reading 20 numbers:")
printArray(alpha)
print("\n\n")
print("Beta after a call to doubleArray:")
beta = doubleArray(alpha, beta)
printArray(beta)
print("", end="\n")
copyGamma(inStock, gamma)
copyAlphaBeta(alpha, beta, inStock)
print("\n")
setInStock(delta, inStock)

#print(len(inStock))