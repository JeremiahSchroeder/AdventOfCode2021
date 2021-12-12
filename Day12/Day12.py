from time import sleep, perf_counter
import numpy

def solution():

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numRows=len(inputStringList)

    caveArray = numpy.empty([numRows,2], dtype=object)

    for i in range(0, numRows):
        caveArray[i,:] = inputStringList[i].replace('\n','').split('-')

    #Organize information into list of all caves
    # and lists of all their connections

    listOfCaves = []
    listOfConnections = []

    for i in range(0, numRows):

        if not caveArray[i,0] in listOfCaves:
            listOfCaves.append(caveArray[i,0])
            listOfConnections.append([caveArray[i,1]])
        else:
            listOfConnections[listOfCaves.index(caveArray[i,0])].append(caveArray[i, 1])
        if not caveArray[i,1] in listOfCaves:
            listOfCaves.append(caveArray[i,1])
            listOfConnections.append([caveArray[i,0]])
        else:
            listOfConnections[listOfCaves.index(caveArray[i,1])].append(caveArray[i, 0])

    listOfPaths = [['start']]
    isPathDone = [False]

    while False in isPathDone:
        for i in range(0, len(listOfPaths)):
            if not isPathDone[i]:
                newBranch = False

                for connection in listOfConnections[listOfCaves.index(listOfPaths[i][-1])]:
                    if connection.isupper() or not connection in listOfPaths[i]:
                        if not newBranch:
                            newBranch = True
                            listOfPaths[i].append(connection)
                            if connection == 'end':
                                isPathDone[i] = True
                        else:
                            listOfPaths.append(listOfPaths[i].copy())
                            listOfPaths[-1][-1]=connection
                            isPathDone.append(False)
                            if connection == 'end':
                                isPathDone[-1] = True
                if not newBranch:
                    isPathDone[i] = True

    listOfCompletePaths = []

    for path in listOfPaths:
        if path[-1] == 'end':
            listOfCompletePaths.append(path)

    print("There are ", len(listOfCompletePaths), "paths out of the caves.")


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)