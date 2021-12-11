from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows=len(inputStringList)
    numColumns = len(inputStringList[0].replace('\n',''))

    energyLevelArray = numpy.zeros([numRows,numColumns], int)

    #get rid of newline Characters
    for i in range (0, numRows):
        inputStringList[i] = inputStringList[i].replace('\n','')
        for j in range(0, numColumns):
            energyLevelArray[i,j] = str(inputStringList[i][j])

    flashCount = 0

    #Steps of flashes
    for step in range(1, 100+1):
        #Initial global energy increase
        energyLevelArray += 1

        #Flash all over 9 and increment adjacent values
        while len(numpy.where(energyLevelArray > 9)[0]) > 0:
            energyLevelArray, flashCount = flash(energyLevelArray,flashCount)

    print(flashCount)

    while len(numpy.where(energyLevelArray != 0)[0]) > 0:
        step += 1
        # Initial global energy increase
        energyLevelArray += 1

        # Flash all over 9 and increment adjacent values
        while len(numpy.where(energyLevelArray > 9)[0]) > 0:
            energyLevelArray, flashCount = flash(energyLevelArray, flashCount)

    print(step)

def flash(energyLevelArray,flashCount):


    #Adjacent Locations
    rowList = [-1, -1, -1, 0, 0, 1, 1, 1]
    columnList = [-1, 0, 1, -1, 1, -1, 0, 1]

    #Step through all locations that flash
    locations = numpy.where(energyLevelArray > 9)
    for i in range(0,len(locations[0])):
        flashLocRow = locations[0][i]
        flashLocCol = locations[1][i]

        energyLevelArray[flashLocRow,flashLocCol] = 0
        flashCount+=1

        #increment all adjacent locations
        for j in range(0, len(rowList)):
            adjLocRow = flashLocRow+rowList[j]
            adjLocCol = flashLocCol+columnList[j]
            if adjLocRow > -1 \
                    and adjLocRow < len(energyLevelArray[0,:]) \
                    and adjLocCol> -1 \
                    and adjLocCol< len(energyLevelArray[:,0])\
                    and energyLevelArray[adjLocRow,adjLocCol] != 0:
                energyLevelArray[adjLocRow,adjLocCol] +=1

    return energyLevelArray, flashCount

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)