from sys import maxsize
from typing import List, Tuple, Optional


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


def unoptimized_shorted_path_in_graph_using_array(start: int, edges) -> List[int | float]:
    """
    You're given an integer start and a list edges of
    pairs of integers.


    The list is what's called an adjacency list, and it represents a graph. The
    number of vertices in the graph is equal to the length of edges,
    where each index i in edges contains vertex
    i's outbound edges, in no particular order. Each individual edge
    is represented by an pair of two numbers,
    [destination, distance], where the destination is a positive
    integer denoting the destination vertex and the distance is a positive integer
    representing the length of the edge (the distance from vertex
    i to vertex destination). Note that these edges are
    directed, meaning that you can only travel from a particular vertex to its
    destination—not the other way around (unless the destination vertex itself has
    an outbound edge to the original vertex).


    Write a function that computes the lengths of the shortest paths between
    start and all of the other vertices in the graph using Dijkstra's
    algorithm and returns them in an array. Each index i in the
    output array should represent the length of the shortest path between
    start and vertex i. If no path is found from
    start to vertex i, then
    output[i] should be -1.


    Note that the graph represented by edges won't contain any
    self-loops (vertices that have an outbound edge to themselves) and will only
    have positively weighted edges (i.e., no negative distances).


    If you're unfamiliar with Dijkstra's algorithm, we recommend watching the
    Conceptual Overview section of this question's video explanation before
    starting to code.

    Sample Input
    start = 0
    edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    [],
    ]

    Sample Output
    [0, 7, 13, 27, 10, -1]
    """
    num_vertices = len(edges)
    min_distances = [float('inf') for _ in range(num_vertices)]
    min_distances[start] = 0
    visited = set()
    def get_vertex_with_min_distance(distances: List[int|float] , visited: set):
        min_distance = float('inf')
        vertex = None

        for vertex_idx, distance in enumerate(distances): # O(v) version that is slow to get min val in the array
            if vertex_idx in visited:
                continue
            if distance <= min_distance:
                vertex = vertex_idx
                min_distance = distance

        return vertex, min_distance
    

    while len(visited) != num_vertices: # O(v) version that is slow
        vertex, current_min_distance = get_vertex_with_min_distance(min_distances, visited) # O(v) as well so currently O(v^2)
        if current_min_distance == float('inf'):
            break
        visited.add(vertex)
        for destination, distance in edges[vertex]: # Including this operation our time complexity is O(v^2 + e)
            if destination in visited:
                continue
            new_path_distance = current_min_distance + distance
            if new_path_distance < min_distances[destination]:
                min_distances[destination] = new_path_distance

    return list(map(lambda x: -1 if x == float('inf') else x, min_distances))


class AEMinHeap_4_dijkstras_algorithm:
    @staticmethod
    def dijkstras_algorithm(start:int, edges: List[List]) -> List[int]:

        min_distances = [maxsize for _ in range(len(edges))]
        min_distances[start] = 0
        default_heap_array = [(idx, maxsize) for idx in range(len(edges))]
        min_distance_heap = AEMinHeap_4_dijkstras_algorithm(default_heap_array)
        min_distance_heap.update_vertex(start, 0)

        while not min_distance_heap.empty():
            try:
                vertex, current_min_distance = min_distance_heap.pop()
                if current_min_distance == maxsize:
                    break
                for destination, distance in edges[vertex]:
                    new_path_distance = current_min_distance + distance
                    if new_path_distance < min_distances[destination]:
                        min_distances[destination] = new_path_distance
                        min_distance_heap.update_vertex(destination, new_path_distance)
            except IndexError:
                print("Attempted to pop from an empty heap")


        return  list(map(lambda x: -1 if x == maxsize else x, min_distances))

    def __init__(self, array: List[Tuple[int,int]]):
        # Holds the position in the heap that each vertex is at
        # Note that our heap is storing tuple of vertex/node distance [(v1, w1), (v2, w2)]
        # Where the position of each tuple is determined by the distance
        # Since our min heap is determined by the min distance to start vertex
        self.vertex_map = {vertex:vertex for vertex in range(len(array))}
        self.heap: List[Tuple[int, int]] = self.build_heap(array)

    def build_heap(self, array: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        first_parent_idx = (len(array)//2) - 1
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array), array)
        return array
    
    def sift_down(self, current_idx, end_idx, heap):
        while True:
            left_child_idx = 2 * current_idx + 1
            right_child_idx = 2 * current_idx + 2
            smallest_dist_idx = current_idx

            if left_child_idx < end_idx and heap[left_child_idx][1] < heap[smallest_dist_idx][1]:
                smallest_dist_idx = left_child_idx
            if right_child_idx < end_idx and heap[right_child_idx][1] < heap[smallest_dist_idx][1]:
                smallest_dist_idx = right_child_idx

            if smallest_dist_idx != current_idx:
                self.swap(smallest_dist_idx, current_idx, heap)
                current_idx = smallest_dist_idx
            else:
                return
        

    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2

        while current_idx > 0 and heap[current_idx][1] < heap[parent_idx][1]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self) -> tuple:
        return self.heap[0]

    def pop(self) -> Tuple[int, int]:
        if self.empty():
            raise IndexError("Cannot pop from an empty heap")
        self.swap(0, len(self.heap)-1, self.heap)
        vertex, min_distance = self.heap.pop()
        self.vertex_map.pop(vertex)
        self.sift_down(0, len(self.heap), self.heap)
        return vertex, min_distance

    def empty(self):
        return len(self.heap) == 0

    def swap(self, i, j, heap):
        self.vertex_map[heap[i][0]] = j
        self.vertex_map[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update_vertex(self, vertex, value):
        self.heap[self.vertex_map[vertex]] = (vertex, value) 
        self.sift_up(self.vertex_map[vertex], self.heap)


    



