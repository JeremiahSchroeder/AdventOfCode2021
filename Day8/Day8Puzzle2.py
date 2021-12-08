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
    outputDecodedString = ['XXXX']*numInputLines

    for i in range(0, numInputLines):
        uniqueDigitsArray[i] = inputStringList[i].split('|')[0].split()
        outputArray[i] = inputStringList[i].split('|')[1].split()


    for i in range(0,numInputLines):
        for j in range(0, 10):
            numSegments = len(uniqueDigitsArray[i,j])
            if numSegments == 3:
                threeDigString = uniqueDigitsArray[i,j]
            elif numSegments == 4:
                fourDigString = uniqueDigitsArray[i,j]

        for j in range(0, numDigits):
            jDigit = outputArray[i,j]
            jLength = len(jDigit)
            outDigit = ''

            if jLength ==2:
                outDigit = '1'
            elif jLength == 3:
                outDigit = '7'
            elif jLength ==4:
                outDigit = '4'
            elif jLength == 7:
                outDigit = '8'
            else:
                threeDigCount = 0
                fourDigCount = 0
                for k in range(0, 3):
                    if threeDigString[k] in jDigit:
                        threeDigCount += 1
                for k in range(0, 4):
                    if fourDigString[k] in jDigit:
                        fourDigCount += 1
                if jLength ==5:
                    if threeDigCount == 3:
                        outDigit = '3'
                    elif fourDigCount == 2:
                        outDigit = '2'
                    else:
                        outDigit = '5'
                else:
                    if fourDigCount ==4:
                        outDigit = '9'
                    elif threeDigCount ==3:
                        outDigit = '0'
                    else:
                        outDigit = '6'
            outputDecodedString[i]=outputDecodedString[i].replace('X',outDigit,1)

    outputIntList = [0]*numInputLines

    print(outputDecodedString)

    for i in range(0, numInputLines):
        outputIntList[i] = int(outputDecodedString[i])

    print(sum(outputIntList))

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)