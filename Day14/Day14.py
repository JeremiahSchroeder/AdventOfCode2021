from time import sleep, perf_counter
import numpy

def solution():

    numSteps = 10
    numStepsPart2 = 40

    inputFile = open('input','r')
    # inputFile = open('inputTest','r')

    inputStringList = inputFile.readlines()

    inputFile.close()

    for i in range(0,len(inputStringList)):
        inputStringList[i] = inputStringList[i].replace('\n','')

    polymer = inputStringList.pop(0)

    inputStringList.pop(0)
    pairList = []
    insertionList = []

    for i in range(0,len(inputStringList)):
        pairList.append(inputStringList[i].split(' -> ')[0])
        insertionList.append(inputStringList[i].split(' -> ')[1])

    # print(polymer)

    for i in range(0, numSteps):
        polymer = polymerInsert(polymer, pairList, insertionList)
        # print(polymer)

    print('Answer Part 1')
    countCharacters(polymer)

    # print('begin part two')
    # lastTime = perf_counter()
    # for i in range(0, numStepsPart2-numSteps):
    #     polymer = polymerInsert(polymer, pairList, insertionList)
    #     print(lastTime - perf_counter())
    #     lastTime = perf_counter()


    # print('Answer Part 2')
    # countCharacters(polymer)


def countCharacters(polymer):
    characterList = []
    characterCount = []
    for i in range(0, len(polymer)):
        if not polymer[i] in characterList:
            characterList.append(polymer[i])
            characterCount.append(polymer.count(polymer[i]))

    print('The most common character is ', characterList[characterCount.index(max(characterCount))],
          ', with ', max(characterCount), ' characters.')
    print('The least common character is ', characterList[characterCount.index(min(characterCount))],
          ', with ', min(characterCount), ' characters.')
    print('The difference is: ', max(characterCount) - min(characterCount))

    return


def polymerInsert(polymer, pairList, insertionList):

    i = 0
    while i < len(polymer)-1:
        polymer = polymer[:i+1] +insertionList[pairList.index(polymer[i:i+2])] + polymer[i+1:]
        i+=2

    return polymer


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)