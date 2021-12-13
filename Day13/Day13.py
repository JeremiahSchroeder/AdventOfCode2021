from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    for i in range(0,len(inputStringList)):
        inputStringList[i] = inputStringList[i].replace('\n','')

    listOfDots = []
    listOfFolds=[]
    for i in range(0,inputStringList.index('')):
        listOfDots.append([
            int(inputStringList[i].split(',')[0]),
            int(inputStringList[i].split(',')[1])])

    for i in range(inputStringList.index('')+1,len(inputStringList)):
        listOfFolds.append([
            inputStringList[i].split()[2].split('=')[0],
            int(inputStringList[i].split()[2].split('=')[1])])

    #assume always folding in half
    if listOfFolds[0][0] == 'x':
        numRows = listOfFolds[1][1]*2+1
        numColumns = listOfFolds[0][1]*2+1
    else:
        numRows = listOfFolds[0][1]*2+1
        numColumns = listOfFolds[1][1]*2+1

    dotArray = numpy.zeros([numRows,numColumns], dtype=bool)

    for i in range(0,len(listOfDots)):
        dotArray[listOfDots[i][1],listOfDots[i][0]] = 1

    dotArray = foldDotArray(dotArray,listOfFolds[0])

    print('The number of dots after 1 fold is:\n', len(numpy.where(dotArray)[0]))

    for i in range(1, len(listOfFolds)):
        dotArray = foldDotArray(dotArray,listOfFolds[i])

    print("The final folded dots show:")
    printDotArray(dotArray)

def printDotArray(dotArray):
    for i in range(0, len(dotArray[:,0])):
        for j in range(0, len(dotArray[0,:])):
            if dotArray[i,j] == 1:
                print('#',end='')
            else:
                print('.',end='')
        print('')

    return

def foldDotArray(dotArray,fold):
    if fold[0] == 'x':
        newDotArray = numpy.array(dotArray[:,0:fold[1]])
        otherHalf = numpy.array(dotArray[:,fold[1]+1:len(dotArray[0,:])])
        otherHalf = numpy.fliplr(otherHalf)

    else:
        newDotArray = numpy.array(dotArray[0:fold[1],:])
        otherHalf = numpy.array(dotArray[fold[1]+1:len(dotArray[:,0]),:])
        otherHalf = numpy.flipud(otherHalf)

    newDotArray = numpy.logical_or(newDotArray,otherHalf)

    return newDotArray

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)