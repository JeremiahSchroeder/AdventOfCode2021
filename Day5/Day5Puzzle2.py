from time import sleep, perf_counter
import numpy


def solution():
    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringArray = inputFile.readlines()

    inputFile.close()

    xArray = numpy.zeros((len(inputStringArray) , 2), int)
    yArray = numpy.zeros((len(inputStringArray) , 2), int)

    for i in range (0, len(inputStringArray)):
        inputStringArray[i] = inputStringArray[i].replace(",", " ")
        inputStringArray[i] = inputStringArray[i].replace('-> ', '')
        inputStringArray[i] = inputStringArray[i].replace('\n', '')
        for j in range(0, 2):
            xArray[i,j] = int((inputStringArray[i]).split()[j*2])
            yArray[i,j] = int((inputStringArray[i]).split()[j*2+1])

    maxX= numpy.amax(xArray)+1
    maxY = numpy.amax(yArray) + 1
    ventCountArray = numpy.zeros((maxY,maxX))

    for i in range (0, len(xArray)):
        if xArray[i,0] == xArray[i,1]:
            x = xArray[i,0]
            for y in range (min(yArray[i,0], yArray[i,1]), max(yArray[i,0], yArray[i,1])+1):
                ventCountArray[y,x] += 1

        elif yArray[i,0] == yArray[i,1]:
            y = yArray[i,0]
            for x in range (min(xArray[i,0], xArray[i,1]), max(xArray[i,0], xArray[i,1])+1):
                ventCountArray[y,x] += 1

        else :
            numVents = max(xArray[i,0], xArray[i,1]) - min(xArray[i,0], xArray[i,1])+1
            xDirection = int((xArray[i, 1] - xArray[i, 0]) / (numVents - 1))
            yDirection = int((yArray[i, 1] - yArray[i, 0]) / (numVents - 1))
            x = xArray[i,0]
            y = yArray[i,0]
            for j in range (0, numVents):
                ventCountArray[y+j*yDirection, x+j*xDirection] += 1

    # print(ventCountArray)
    print(len(numpy.where(ventCountArray > 1)[0]))



start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)