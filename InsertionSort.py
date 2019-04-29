# insertion sort
# Sophia Quick
import random
import time
import matplotlib.pyplot as pyplot


# this is my implementation of insertion sort
def insertionSort(nums):
    sorting_num = 0
    high_idx = len(nums)
    # Loop through each index in list
    while sorting_num < high_idx:
        # if first item in list, immediately move right
        if sorting_num > 0:
            idx_holder = sorting_num
            # Loop until number to left is smaller
            while nums[sorting_num] < nums[sorting_num - 1]:
                holder = nums[sorting_num]
                nums[sorting_num] = nums[sorting_num - 1]
                nums[sorting_num - 1] = holder
                if sorting_num > 1:
                    sorting_num -= 1
            sorting_num = idx_holder + 1
        else:
            sorting_num += 1
    return nums


# this is my worst case generator
def worstCase(n):
    nums = list(range(1, n + 1))
    # puts list in backwards order
    reversed_nums = list(reversed(nums))
    return reversed_nums


# this is my best case generator
def bestCase(n):
    nums = list(range(1, n + 1))
    return nums


# this is my random generator
def randomCase(n):
    nums = []
    #creates list of size n with random number ranging from 0 to n*10
    for i in range(n):
        nums.append(random.randint(0, 10 * n))
    return nums

def test( fn, N ):
    start_time = time.process_time()
    nums = fn(N)
    insertionSort(nums)
    end_time = time.process_time()
    return ( ( end_time - start_time ) )


def main():
    print("Times from different generators:")

    # Arrays to store results and x-axis points
    Ns = []
    BestCase = []
    WorstCase = []
    RandomCase = []

    # The actual tests being performed for each "trial"
    TRIALS = [10, 20, 50, 100, 1000, 2000, 5000, 7000, 10000]
    for i in TRIALS:
        Ns.append(i)
        timeWorstCase = test(worstCase, i)
        timeBestCase = test(bestCase, i)
        timeRandomCase = test(randomCase, i)
        BestCase.append(timeBestCase)
        WorstCase.append(timeWorstCase)
        RandomCase.append(timeRandomCase)
        # prints times for each trial
        print("Best Case: %20g     Worst Case: %20g      Random: %20g" % (timeBestCase, timeWorstCase, timeRandomCase))

    # Plot results on single graph
    pyplot.plot(Ns, BestCase, color="blue")
    pyplot.plot(Ns, WorstCase, color="red")
    pyplot.plot(Ns, RandomCase, color="green")
    pyplot.axis([100, None, 0, None])
    pyplot.show()

    pyplot.plot(Ns, BestCase, color="blue")
    pyplot.show()






if __name__ == "__main__": main()
