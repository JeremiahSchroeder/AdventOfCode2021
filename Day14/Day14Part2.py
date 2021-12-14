from time import sleep, perf_counter
import numpy

def solution():

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

    characterList = []
    characterCount = []

    for i in range(0, len(polymer)-1):
        polymerInsert(polymer[i:i+2], pairList, insertionList, 0, numStepsPart2, characterList, characterCount)

    characterCount[characterList.index(polymer[0])]+=1

    print('The most common character is ', characterList[characterCount.index(max(characterCount))],
          ', with ', max(characterCount), ' characters.')
    print('The least common character is ', characterList[characterCount.index(min(characterCount))],
          ', with ', min(characterCount), ' characters.')
    print('The difference is: ', max(characterCount) - min(characterCount))

def polymerInsert(pair, pairList, insertionList, step, maxSteps, characterList, characterCount):

    pair1 = pair[0]+insertionList[pairList.index(pair)]
    pair2 = pair1[1]+pair[1]

    step+=1

    if step == maxSteps:
        if not pair1[1] in characterList:
            characterList.append(pair1[1])
            characterCount.append(1)
        else:
            characterCount[characterList.index(pair1[1])]+=1
        if not pair2[1] in characterList:
            characterList.append(pair2[1])
            characterCount.append(1)
        else:
            characterCount[characterList.index(pair2[1])]+=1
    else:
        polymerInsert(pair1, pairList, insertionList, step, maxSteps, characterList, characterCount)
        polymerInsert(pair2, pairList, insertionList, step, maxSteps, characterList, characterCount)
    return


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)