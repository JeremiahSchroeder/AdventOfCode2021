from time import sleep, perf_counter

def solution():
    DepthInput = open('InputDay1Puzzle1','r')
    # DepthInput = open('test','r')
    DepthArray = DepthInput.readlines()
    DepthInput.close()

    numIncreased = 0
    count = 0

    Window = 3

    for i in range (0, len(DepthArray)-Window):
        sum1 = 0
        sum2 = 0

        for j in range(i, i+Window):
            sum1+=int(DepthArray[j])
            sum2+=int(DepthArray[j+1])

        if sum2 > sum1:
            numIncreased+=1

        count+=1


    print(numIncreased)
    print(count)

start = perf_counter()
solution()
end = perf_counter()
execution_time = (end - start)
print(execution_time)