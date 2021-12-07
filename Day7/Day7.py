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

    crabPositionArray = numpy.array(inputString[0].split(','),int)

    fuel = [0]*max(crabPositionArray)

    for position in range (0,max(crabPositionArray)):
        for i in range (0, len(crabPositionArray)):
            fuel[position] += abs(position-crabPositionArray[i])

    print("It takes ", min(fuel)," fuel to get to position ", fuel.index(min(fuel)),".")

    fuelPart2 = [0] * max(crabPositionArray)

    for position in range (0,max(crabPositionArray)):
        for i in range (0, len(crabPositionArray)):
            fuelPart2[position] += sum(range(1, abs(position-crabPositionArray[i])+1))

    print("It takes ", min(fuelPart2), " fuel to get to position ", fuelPart2.index(min(fuelPart2)), " for part two.")

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)