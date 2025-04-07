import pytest

from typing import List

from src.search.binary_search import Search




sorted_search_test_cases = [
    # Basic Found
    ([2, 5, 7, 8, 11, 12], 7, 2),  # 0
    ([2, 5, 7, 8, 11, 12], 2, 0),  # 1
    ([2, 5, 7, 8, 11, 12], 12, 5), # 2


    # Not Found 
    ([2, 5, 7, 8, 11, 12], 13, -1), # 3
    ([2, 5, 7, 8, 11, 12], 0, -1),  # 4
    ([2, 5, 7, 8, 11, 12], 6, -1),  # 5

    # Edge Cases
    ([], 5, -1), # 6
    ([5], 5, 0), # 7
    ([5], 3, -1),# 8

    # Duplicates. At least *an* instance will be found
    ([1, 2, 2, 2, 3], 2, 2), # 9
    ([2, 2, 2, 2, 2], 2, 2), # 10
    ([1, 1, 2, 2, 3], 1, 0), # 11
    ([1, 1, 2, 3, 3], 3, 3), # 12

    # Longer List
    (list(range(0, 100, 2)), 50, 25), # 13
    (list(range(0, 100, 2)), 51, -1), # 14

]

class TestSearch:


    @pytest.mark.parametrize("nums, target, expected_idx", sorted_search_test_cases)
    def test_binary_search_iterative(self, nums: List[int], target:int, expected_idx: int):
        assert Search.binary_search_iterative(nums, target) == expected_idx

    @pytest.mark.parametrize("nums, target, expected_idx", sorted_search_test_cases)
    def test_binary_search_recursive(self, nums: List[int], target:int, expected_idx: int):
        assert Search.binary_search_iterative(nums, target) == expected_idx

