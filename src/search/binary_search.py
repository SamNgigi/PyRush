from typing import List


def binary_search_iterative(nums: List[int], target: int) -> int:
    
    start: int = 0;
    end: int = len(nums) - 1

    while start <= end:
        
        mid: int = (start + end) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binary_search_recursive(nums: List[int], target: int) -> int:
    
    start: int = 0
    stop: int = len(nums) - 1

    def bin_search_helper(nums: List[int], target: int, start: int, stop: int) -> int:
        
        if start > stop:
            return -1

        mid: int = (start + stop) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return bin_search_helper(nums, target, mid + 1, stop)
        else:
            return bin_search_helper(nums, target, start, mid - 1)

    return bin_search_helper(nums, target, start, stop)


