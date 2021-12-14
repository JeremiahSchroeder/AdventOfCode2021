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
    childPairList = []
    pairCount = []

    for i in range(0,len(inputStringList)):
        pair = inputStringList[i].split(' -> ')[0]
        insertion = inputStringList[i].split(' -> ')[1]
        childPair1 =pair[0]+insertion
        childPair2 = insertion + pair[1]

        pairList.append(pair)
        childPairList.append([childPair1, childPair2])
        pairCount.append(0)

    for i in range(0, len(polymer)-1):
        pairCount[pairList.index(polymer[i:i+2])]+=1

    for i in range(0, numStepsPart2):
        pairCount = polymerInsert(pairCount,pairList,childPairList)

    characterList = [polymer[0]]
    characterCount = [1]

    for i in range(0, len(pairCount)):
        secondChar = pairList[i][1]
        count = pairCount[i]
        if not secondChar in characterList:
            characterList.append(secondChar)
            characterCount.append(count)
        else:
            characterCount[characterList.index(secondChar)] += count


    print('The answer is: ', max(characterCount)-min(characterCount),'.')



def polymerInsert(pairCount, pairList, childPairList):
    pairCount2 = [0]*len(pairCount)

    for i in range(0, len(pairCount)):
        count = pairCount[i]
        childPair1Index = pairList.index(childPairList[i][0])
        childPair2Index = pairList.index(childPairList[i][1])

        pairCount2[childPair1Index]+=count
        pairCount2[childPair2Index]+=count

    return pairCount2





start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)