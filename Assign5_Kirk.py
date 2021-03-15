""" 
Author: Jamey Kirk
Title: Assignment5_Lists
Date: 03/14/2021
Description: tests the function main and other array functions 
"""

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
    for row in range(len(stockList)):
        col = 0
        while col < len(gammaList):
            if row == 0:
                stockList[row][col] = gammaList[col]
            else:
                stockList[row][col] = gammaList[col] * pow(3, row) 
            col += 1
    return stockList

def copyAlphaBeta (aList, bList, inList):
    """
    stores alpha into the first five rows of inStock and beta into the last 
    five rows of inStock
    """
    row = 0
    while row < len(inList) / 2:
        col = 0
        while col < len(inList[0]):
            inList[row][col] = aList[col + (row * 4)]
            inList[row + 5][col] = bList[col + (row * 4)]
            col += 1
        row += 1
    return inList

def printArray (oneDList):
    """
    prints any one-dimensional list
    """
    for index in oneDList:
        print(index, end="\t")

def setInStock ():
    pass

inStock = [[None for x in range(4)] for y in range(10)]
alpha = [None for x in range(20)]
beta = [None for x in range(20)]
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

print("Alpha after initialization:")
printArray(setZero(alpha))
print("", end="\n\n")
alpha = inputArray(alpha)
print("", end="\n")
print("Alpha after reading 20 numbers:")
printArray(alpha)
print("", end="\n\n")
print("Beta after a call to doubleArray:")
printArray(doubleArray(alpha, beta))
print("", end="\n\n")
print("inStock after a call to copyGamma:")
print(copyGamma(inStock, gamma))
print("", end="\n\n")
print("inStock after a call to copyAlphaBeta:")
print(copyAlphaBeta(alpha, beta, inStock))
print("", end="\n\n")
print("inStock after a call to setInStock:")


#print(len(inStock))