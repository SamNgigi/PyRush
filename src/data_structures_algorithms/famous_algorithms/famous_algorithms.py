from typing import List


def ae_kadanes_algorithm(array: List[int]):
    """
    Write a function that takes in a non-empty array of integers and returns the
    maximum sum that can be obtained by summing up all of the integers in a
    non-empty subarray of the input array. A subarray must only contain adjacent
    numbers (numbers next to each other in the input array).

    Sample Input
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

    Sample Output
    19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]
    """
    current_max, final_max = array[0], array[0]
    for i in range(1, len(array)):
        current_max = max(array[i], array[i] + current_max)
        final_max = max(current_max, final_max)

    return final_max
