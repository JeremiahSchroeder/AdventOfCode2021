from time import sleep, perf_counter
import numpy

def solution():
    # bingoNumbersFile = open('bingoNumbersTest','r')
    # bingoCardsFile = open('bingoCardsTest','r')
    bingoNumbersFile = open('bingoNumbers','r')
    bingoCardsFile = open('bingoCards','r')

    bingoNumbersString = bingoNumbersFile.readlines()
    bingoCardsStringList = bingoCardsFile.readlines()
    bingoNumbersFile.close()
    bingoCardsFile.close()

    bingoNumbersList = ((bingoNumbersString[0]).replace(',',' ')).split()
    for i in range (0, len(bingoNumbersList)):
        bingoNumbersList[i] = int(bingoNumbersList[i])

    numBingoCards =int(len(bingoCardsStringList)/6)

    bingoCardArray = numpy.zeros((numBingoCards,5,5),int)
    numberIsNotCalled = numpy.ones((numBingoCards,5,5),int)
    hasNotWon = numpy.ones(numBingoCards,int)


    for i in range (0,numBingoCards):
        for j in range(0, 5):
            for k in range(0,5):
                bingoCardArray[i,j,k] = int(str(bingoCardsStringList[i*6+j+1]).split()[k])


    for numberIndex in range (0, len(bingoNumbersList)):
        if numpy.sum(hasNotWon) == 0:
            break

        for i in range(0, numBingoCards):
            if hasNotWon[i] == 0:
                continue

            for j in range(0, 5):
                for k in range(0, 5):
                    if bingoCardArray[i,j,k] == bingoNumbersList[numberIndex]:
                        numberIsNotCalled[i,j,k] = 0

            for j in range(0,5):
                if numpy.sum(numberIsNotCalled[i,j,:]) == 0:

                    hasNotWon[i] = 0
                    if numpy.sum(hasNotWon) ==0:
                        remainingnumbers = bingoCardArray[i, :, :] * numberIsNotCalled[i, :, :]
                        sum = numpy.sum(remainingnumbers)
                        answer = bingoNumbersList[numberIndex] * sum
                        print('The answer is: ', answer)
                    break

            for k in range(0, 5):
                if hasNotWon[i] ==0:
                    break
                if numpy.sum(numberIsNotCalled[i, :, k]) == 0:
                    hasNotWon[i] = 0
                    if numpy.sum(hasNotWon) ==0:
                        remainingnumbers = bingoCardArray[i, :, :] * numberIsNotCalled[i, :, :]
                        sum = numpy.sum(remainingnumbers)
                        answer = bingoNumbersList[numberIndex] * sum
                        print('The answer is: ', answer)
                    break


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)