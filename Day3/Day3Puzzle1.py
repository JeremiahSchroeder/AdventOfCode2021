from time import sleep, perf_counter

def solution():
    inputFile = open('input','r')
    # inputFile = open('test','r')
    inputArray = inputFile.readlines()
    inputFile.close()

    gammaRate = ''
    epsilonRate = ''

    numDigits = len(inputArray[0].rstrip("\n"))

    for i in range (0, numDigits):
        numOnes = 0

        for j in range (0, len(inputArray)):
            numOnes += int((inputArray[j])[i])

        if numOnes >= len(inputArray)-numOnes:
            gammaRate+='1'
            epsilonRate+='0'

        else :
            gammaRate+='0'
            epsilonRate+='1'

    print(gammaRate)
    print(epsilonRate)
    print(int(gammaRate,2)*int(epsilonRate,2))

    print('Part 2')

    oxGenArray = inputArray[:]
    co2Array = inputArray[:]

    for i in range (0, numDigits):
        numOnes = 0

        for j in range (0, len(oxGenArray)):
            numOnes += int((oxGenArray[j])[i])

        if numOnes >= len(oxGenArray)-numOnes:
            digit = '1'
        else:
            digit = '0'

        j = 0

        while j < len(oxGenArray):

            if (oxGenArray[j])[i] == digit:
                j += 1
            else :
                del oxGenArray[j]

        if len(oxGenArray) == 1:
            break

    for i in range (0, numDigits):
        numOnes = 0


        for j in range (0, len(co2Array)):
            numOnes += int((co2Array[j])[i])
        if numOnes >= len(co2Array)-numOnes:
            digit = '0'
        else:
            digit = '1'
        j = 0

        while j < len(co2Array):

            if (co2Array[j])[i] == digit:
                j += 1
            else :
                del co2Array[j]

        if len(co2Array) == 1:
            break

    print(int(oxGenArray[0],2)*int(co2Array[0],2))


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)

