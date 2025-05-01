from typing import List
from collections import deque


class AENodeGraph:
    """
      You're given a Node class that has a name and an
      array of optional children nodes. When put together, nodes form
      an acyclic tree-like structure.


      Implement the depthFirstSearch method on the
      Node class, which takes in an empty array, traverses the tree
      using the Depth-first Search approach (specifically navigating the tree from
      left to right), stores all of the nodes' names in the input array, and returns
      it.


      If you're unfamiliar with Depth-first Search, we recommend watching the
      Conceptual Overview section of this question's video explanation before
      starting to code.

    Sample Input
    graph = A
         /  | \
        B   C   D
       /\\     / \
      E   F   G   H
         /\\   \
        I   J   K

    Sample Output
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

    """

    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(AENodeGraph(name))
        return self
    
    def depth_first_search_recursive(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

    def depth_first_search_iterative(self, array):
        stack = deque([self])

        while stack:
            current = stack.pop()
            array.append(current.name)
            for child in reversed(current.children):
                stack.append(child)
        return array
    
    def breadth_first_search(self, array):
        queue = deque([self])

        while queue:
            current = queue.popleft()
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array

def has_single_cycle_med(array: list) -> bool:
    """
    You're given an array of integers where each integer represents a jump of its
    value in the array. For instance, the integer 2 represents a jump
    of two indices forward in the array; the integer -3 represents a
    jump of three indices backward in the array.


    If a jump spills past the array's bounds, it wraps over to the other side. For
    instance, a jump of -1 at index 0 brings us to the last index in
    the array. Similarly, a jump of 1 at the last index in the array brings us to
    index 0.


    Write a function that returns a boolean representing whether the jumps in the
    array form a single cycle. A single cycle occurs if, starting at any index in
    the array and following the jumps, every element in the array is visited
    exactly once before landing back on the starting index.

    Sample Input
    array = [2, 3, 1, -4, -4, 2]

    Sample Output
    true
    """
    def get_next_idx(current_idx: int):
        # In python the modulo the direction of the modulo is determined by the divisor
        # If the divisor is positive the direction will always be positive even when the
        # dividend is negative. Other languages for the below to work we offset with by
        # adding back the array length
        jump: int = array[current_idx]
        next_idx: int = (current_idx + jump) % len(array)
        return next_idx

    visited_elements = 0
    idx = 0
    while True:
        idx: int = get_next_idx(idx)
        visited_elements += 1
        if idx == 0 or array[idx] == 0 or visited_elements > len(array):
            break

    return visited_elements == len(array)

def river_sizes_med(matrix: List[List[int]]) -> List[int]:
    """
        You're given a two-dimensional array (a matrix) of potentially unequal height

        and width containing only 0s and 1s. Each
        0 represents land, and each 1 represents part of a
        river. A river consists of any number of 1s that are either
        horizontally or vertically adjacent (but not diagonally adjacent). The number

        of adjacent 1s forming a river determine its size.


        Note that a river can twist. In other words, it doesn't have to be a straight

        vertical line or a straight horizontal line; it can be L-shaped, for example.



        Write a function that returns an array of the sizes of all rivers represented

        in the input matrix. The sizes don't need to be in any particular order.

        Sample Input
        matrix = [
          [1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 0],
        ]

        Sample Output
        [1, 2, 2, 2, 5] // The numbers could be ordered differently.


        // The rivers can be clearly seen here:
        // [
        //   [1,  ,  , 1,  ],
        //   [1,  , 1,  ,  ],
        //   [ ,  , 1,  , 1],
        //   [1,  , 1,  , 1],
        //   [1,  , 1, 1,  ],
        // ]

    """
    
    ROWS, COLS = len(matrix), len(matrix[0])
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    sizes_array = []

    def bfs(row, col):
        queue = deque([(row, col)])
        visited.add((row, col))
        size = 0

        while queue:
            cr, cc = queue.popleft()
            size += 1
            for r, c in neighbors:
                nr, nc = cr + r, cc + c
                if(
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and
                    matrix[nr][nc] == 1 and
                    (nr, nc) not in visited
                ):
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        sizes_array.append(size)

    for row in range(ROWS):
        for col in range(COLS):
            if(matrix[row][col] == 1 and (row, col) not in visited):
                bfs(row, col)

    return sizes_array



