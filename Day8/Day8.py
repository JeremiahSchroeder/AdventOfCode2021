from time import sleep, perf_counter
import numpy

def solution():
    numDigits = 4

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    numInputLines=len(inputStringList)

    uniqueDigitsArray = numpy.empty([numInputLines, 10], dtype='U7')
    outputArray = numpy.empty([numInputLines, numDigits], dtype='U7')

    for i in range(0, numInputLines):
        uniqueDigitsArray[i] = inputStringList[i].split('|')[0].split()
        outputArray[i] = inputStringList[i].split('|')[1].split()

    countOf1478 = 0
    for i in range(0,numInputLines):
        for j in range(0, numDigits):
            numSegments = len(outputArray[i,j])
            if numSegments == 2 or numSegments == 3 or numSegments == 4 or numSegments == 7:
                countOf1478 += 1

    print(countOf1478)

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)