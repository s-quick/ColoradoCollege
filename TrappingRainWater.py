import random
import time
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt


def TrappingRainWater(arr):
    start_time = time.process_time()
    max_left = []
    max_right = [0 for i in range(len(arr))]
    total_sum = 0

    max_left.append(arr[0])
    for i in range(1, len(arr)):
        max_left.append(max(max_left[i-1], arr[i]))

    max_right[-1] = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        max_right[i] = max(max_right[i+1], arr[i])

    for num in range(0, len(arr)):
        current = min(max_left[num], max_right[num]) - arr[num]
        if (current > 0):
            total_sum += current

    end_time = time.process_time()

    #return for grpahing time
    #1000 * end_time - start_time

    return total_sum

def BruteForce(arr):
    start_time = time.process_time()
    total_sum = 0

    for num in range(0, len(arr)):
        left_max = 0
        right_max = 0
        for i in range (0, num+1):
            if i > left_max:
                left_max = i
        for j in range (num+1, len(arr)):
            if j > right_max:
                right_max = j
        current = min(left_max, right_max) - arr[num]
        if (current > 0):
            total_sum += current
    #print(total_sum)

    end_time = time.process_time()

    return 1000 * end_time-start_time

def testNoShuffle(N):
    nums = []
    for i in range(N):
        nums.append(random.randint(0, 10 * N))
    return nums

def testShuffle(N):
    nums = []
    for i in range(N):
        nums.append(random.randint(0, 100 * N))
    random.shuffle(nums)
    return nums

def main():
    sizes = [10, 100, 1000, 5000, 10000]
    TRW_results = []
    BF_results = []
    for i in sizes:
        TRW_results.append(TrappingRainWater(testNoShuffle(i)))
    for j in sizes:
        BF_results.append(BruteForce(testNoShuffle(j)))

    AGAINS = 100
    TRW_no_shuffle = []
    TRW_shuffle = []
    for i in range(0, AGAINS):
        TRW_no_shuffle.append(TrappingRainWater(testNoShuffle(1000)))

    for i in range(0, AGAINS):
        TRW_shuffle.append(TrappingRainWater(testNoShuffle(1000)))

    #These are graphs for comparing time for brute force to dynamic
    # pyplot.plot(sizes, TRW_results, color="red")
    # #same scale as brute force results on y-axis
    # #pyplot.ylim(0, 38000)
    # pyplot.show()
    # pyplot.plot(sizes, BF_results, color="blue")
    # pyplot.show()


    plt.plot(TRW_no_shuffle, 'ro')
    plt.plot(TRW_shuffle, 'bo')
    plt.show()

if __name__== "__main__":
    main()

