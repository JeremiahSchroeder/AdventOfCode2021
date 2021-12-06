from time import sleep, perf_counter
import numpy


def solution():
    numDays = 256
    newbornGest = 8
    adultGest = 6

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputString = inputFile.readlines()

    inputFile.close()

    gestationTimeArray = numpy.array(inputString[0].split(','),int)

    summedGestTimeArray = [0]*(newbornGest+1)



    for i in range (0, newbornGest+1):
        summedGestTimeArray[i] = len(numpy.where(gestationTimeArray == i)[0])

    print(summedGestTimeArray)

    for day in range (0, numDays):
        print('day ',day)

        newborns = summedGestTimeArray.pop(0)
        summedGestTimeArray.append(newborns)
        summedGestTimeArray[adultGest]+= newborns

        print(summedGestTimeArray)

    print(summedGestTimeArray)

    print(sum(summedGestTimeArray))

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)