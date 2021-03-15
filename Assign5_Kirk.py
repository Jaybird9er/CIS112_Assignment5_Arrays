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
    userInput = 0
    print("Enter 20 integers:")
    while userInput < len(userArr):
        userArr[userInput] = int(input())
        userInput += 1

def doubleArray (baseList, dubList):
    for item in range(len(baseList)):
        dubList[item] = baseList[item] * 2
    return dubList

def copyGamma (stockList, gammaList):
    for row in range(len(stockList)):
        col = 0
        while col < len(gammaList):
            if row == 0:
                stockList[row][col] = gammaList[col]
            else:
                stockList[row][col] = gammaList[col] * pow(3, row) 
            col += 1
    return stockList

def copyAlphaBeta ():
    pass

def printArray ():
    pass

def setInStock ():
    pass

inStock = [[None for x in range(4)] for y in range(10)]
alpha = [None for x in range(20)]
beta = [None for x in range(20)]
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

#print(inputArray(alpha))
#print(doubleArray(alpha, beta))
#print(copyGamma(inStock, gamma))

#print(len(inStock))