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
    smallDoubleVisit =[False]


    while False in isPathDone:
        for i in range(0, len(listOfPaths)):
            if not isPathDone[i]:
                newBranch = False

                smallDoubleVisitIndex = smallDoubleVisit[i]
                for connection in listOfConnections[listOfCaves.index(listOfPaths[i][-1])]:

                    if (connection.isupper() or not connection in listOfPaths[i] or not smallDoubleVisitIndex) and connection != 'start':
                        if not newBranch:
                            newBranch = True
                            if connection in listOfPaths[i] and connection.islower():
                                smallDoubleVisit[i] = True
                            listOfPaths[i].append(connection)

                            if connection == 'end':
                                isPathDone[i] = True

                        else:
                            smallDoubleVisit.append(smallDoubleVisitIndex)
                            listOfPaths.append(listOfPaths[i].copy())
                            listOfPaths[-1][-1] = ''
                            if connection in listOfPaths[-1] and connection.islower():
                                smallDoubleVisit[-1] = True
                            listOfPaths[-1][-1] = connection
                            isPathDone.append(False)

                            if connection == 'end':
                                isPathDone[-1] = True

                if not newBranch:
                    isPathDone[i] = True

    listOfCompletePaths = []
    listOfcompletPathsStr = []


    for path in listOfPaths:
        # print(path)
        if path[-1] == 'end':
            listOfCompletePaths.append(path)
            # pathStr = ''
            # for cave in path:
            #     pathStr += cave
            #     pathStr += ','
            # listOfcompletPathsStr.append(pathStr)

    # listOfcompletPathsStr.sort()

    # for path in listOfcompletPathsStr:
    #     print(path)

    print("There are ", len(listOfCompletePaths), "paths out of the caves.")



start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)