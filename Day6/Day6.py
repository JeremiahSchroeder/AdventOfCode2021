from time import sleep, perf_counter
import numpy


def solution():
    numDays = 80

    # inputFile = open('input','r')
    inputFile = open('inputTest','r')

    inputString = inputFile.readlines()

    inputFile.close()

    gestationTimeArray = numpy.array(inputString[0].split(','),int)

    for x in range (0, numDays):
        print('Day ', x)
        for i in range (0, len(gestationTimeArray)):
            if gestationTimeArray[i] == 0:
                gestationTimeArray[i] = 6
                gestationTimeArray = numpy.append(gestationTimeArray,8)
            else:
                gestationTimeArray[i] -= 1

    print(len(gestationTimeArray))

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)