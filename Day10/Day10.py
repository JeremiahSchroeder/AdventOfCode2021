from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows=len(inputStringList)

    closingBracketList = [')', ']', '}', '>']
    openingBracketList = ['(', '[', '{', '<']
    pointList = [3, 57, 1197, 25137]
    autoCompletePointList = [1, 2, 3, 4]

    #get rid of newline Characters
    for i in range (0, numRows):
        inputStringList[i] = inputStringList[i].replace('\n','')

    sumPoints = 0
    AutoCompPointsList = []

    #Step through each line
    for line in inputStringList:
        #create empty list to keep track of expected closing brackets
        stack = []
        numCharacters = len(line)

        isCorrupt = False

        #step through each character in the line
        for i in range (0, numCharacters):
            iChar = line[i]
            if iChar in openingBracketList:
                #add expected closing bracket to stack
                stack.append(closingBracketList[openingBracketList.index(iChar)])
            else:
                #Found a closing bracket
                #Remove last expected closing bracket from stack
                #and compare to current character
                lastOpen=stack.pop()
                if iChar != lastOpen:
                    sumPoints += pointList[closingBracketList.index(iChar)]
                    isCorrupt = True
                    break

        #For lines needing completion
        #pop remaining expected closing brackets
        #to find the lines score
        if not isCorrupt:
            AutoCompPoints = 0
            while len(stack) !=0:
                AutoCompPoints *=5
                AutoCompPoints += autoCompletePointList[closingBracketList.index(stack.pop())]
            AutoCompPointsList.append(AutoCompPoints)

    #Get middle value of auto complete points list
    AutoCompPointsList.sort()
    middleIndex = int(len(AutoCompPointsList)/2)

    print('Part one: ', sumPoints)
    print('Part two: ', AutoCompPointsList[middleIndex])

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)