from typing import List

def array_subset(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

     

    Example 1:

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Example 2:

    Input: nums = [0]
    Output: [[],[0]]
     

    Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
    """
    result = []

    def helper(idx: int, subset: List[int]):
        if idx == len(nums):
            result.append(subset[::])
            return
        # Don't pick a number and recurse
        helper(idx + 1, subset)
        # Pick a number and recurse
        subset.append(nums[idx])
        helper(idx + 1, subset)
        # Backtrack and undo picking
        subset.pop()

    helper(0, [])
    return result
