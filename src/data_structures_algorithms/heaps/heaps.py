from typing import List


class AEMinHeap:
    """
    Implement a MinHeap class that supports:

      - Building a Min Heap from an input array of integers.
      - Inserting integers in the heap.
      - Removing the heap's minimum / root value.
      - Peeking at the heap's minimum / root value.
      - Sifting integers up and down the heap, which is to be used when inserting
        and removing values.


    NOTE: heap should be represented in the form of an array.
    
    Computing child nodes is well understood given an array since
    at idx `i`;
        - Child 1 -> 2i + 1
        - Child 2 -> 2i + 2
    Inversly locating the parent node is given by
        floor((i - 1)//2)
    
    Sample Usage
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

    // All operations below are performed sequentially.
    MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
    buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
    insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
    peek(): -5
    remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
    peek(): 2
    remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
    peek(): 6
    insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
    """
    def __init__(self, array: List[int]):
        self.heap: List[int] = self.build_heap(array)

    def build_heap(self, array: List[int]) -> List[int]:
        first_parent =(len(array) // 2) - 1 # -2 if to faciliate flooring of both children accurately
        for current_idx in reversed(range(first_parent + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    def sift_down(self, current_idx: int, end_idx: int, heap: List[int]):
        while True:
            left_child_idx = 2 * current_idx + 1
            right_child_idx = 2 * current_idx + 2
            current_smallest_val_idx = current_idx 

            if left_child_idx < end_idx and heap[left_child_idx] < heap[current_smallest_val_idx]:
                current_smallest_val_idx = left_child_idx
            if right_child_idx < end_idx and heap[right_child_idx] < heap[current_smallest_val_idx]:
                current_smallest_val_idx = right_child_idx

            if current_smallest_val_idx != current_idx: # We need to update the min heap with the current_smallest val
                self.swap(current_smallest_val_idx, current_idx, heap)
                current_idx = current_smallest_val_idx
            else:
                return



    def sift_up(self, current_idx: int, heap: List[int]):
        parent_idx = (current_idx - 1) // 2 # Get parent node

        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx # Get new current node that was previous parent
            parent_idx = (current_idx - 1) // 2 # Get new parent node
        

    def peek(self) -> int:
        if not self.heap: return -1
        return self.heap[0]

    def remove(self):
        pass

    def insert(self, value: int):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i: int, j: int, heap: List[int]):
        heap[i], heap[j] = heap[j], heap[i]
        
