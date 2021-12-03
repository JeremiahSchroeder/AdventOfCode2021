from time import sleep, perf_counter

def solution():
    inputFile = open('input','r')
    # inputFile = open('test','r')
    inputArray = inputFile.readlines()
    inputFile.close()

    forwardPos = 0
    depthPos = 0

    for i in range (0, len(inputArray)):
        direction = str(inputArray[i]).split()[0]
        distance = int(str(inputArray[i]).split()[1])

        if direction == 'forward':
            forwardPos+=distance
        elif direction == 'up':
            depthPos -= distance
        else:
            depthPos +=distance

    print(forwardPos)
    print(depthPos)
    print(forwardPos*depthPos)


start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)