from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows=len(inputStringList)

    #get rid of newline Characters
    for i in range (0, numRows):
        inputStringList[i] = inputStringList[i].replace('\n','')

    numColumns = len(inputStringList[0])
    heightArray = numpy.zeros([numRows, numColumns], int)

    #Get single digits into an array
    for i in range( 0 , numRows):
        for j in range( 0 , numColumns):
            heightArray[i,j] = (inputStringList[i])[j]

    # CalculateRiskLevelSum
    riskLevelSum = 0
    basinSizeList = []
    for i in range( 0 , numRows):
        for j in range( 0 , numColumns):

            #find if adjacent values lower
            above = False
            below = False
            left = False
            right = False

            if i ==0:
                above = True
            else:
                above = heightArray[i,j] < heightArray[i-1,j]
            if i == numRows -1:
                below = True
            else:
                below = heightArray[i, j] < heightArray[i + 1, j]

            if j == 0:
                left = True
            else:
                left = heightArray[i, j] < heightArray[i , j-1]

            if j == numColumns - 1:
                right = True
            else:
                right = heightArray[i, j] < heightArray[i , j+1]

            #low point found
            if above and below and left and right:
                #inpcrment Risk Level Sum
                riskLevelSum += heightArray[i,j]+1

                #Find number of locations in basin
                listGrowing = True
                inBasinList = [[i,j]]

                lastLength = len(inBasinList)
                while listGrowing:

                    for k in range (0, lastLength):
                        aboveCoordinate = [inBasinList[k][0] - 1, inBasinList[k][1]]
                        belowCoordinate = [inBasinList[k][0] + 1, inBasinList[k][1]]
                        leftCoordinate =  [inBasinList[k][0] , inBasinList[k][1] - 1]
                        rightCoordinate = [inBasinList[k][0] , inBasinList[k][1] +1]

                        if not( aboveCoordinate in inBasinList):
                            if aboveCoordinate[0] !=-1:
                                if heightArray[aboveCoordinate[0],aboveCoordinate[1]] != 9:
                                    inBasinList.append(aboveCoordinate)
                        if not( belowCoordinate in inBasinList):
                            if belowCoordinate[0] != numRows:
                                if heightArray[belowCoordinate[0],belowCoordinate[1]] != 9:
                                    inBasinList.append(belowCoordinate)
                        if not( leftCoordinate in inBasinList):
                            if leftCoordinate[1] !=-1:
                                if heightArray[leftCoordinate[0],leftCoordinate[1]] != 9:
                                    inBasinList.append(leftCoordinate)
                        if not( rightCoordinate in inBasinList):
                            if rightCoordinate[1] != numColumns:
                                if heightArray[rightCoordinate[0],rightCoordinate[1]] != 9:
                                    inBasinList.append(rightCoordinate)

                    if len(inBasinList) == lastLength:
                        listGrowing = False

                    lastLength = len(inBasinList)

                basinSizeList.append(lastLength)

    print(basinSizeList)
    productMaxThree = 1
    for i in range(0, 3):
        productMaxThree *= max(basinSizeList)
        basinSizeList.remove(max(basinSizeList))

    print(riskLevelSum)
    print(productMaxThree)

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)