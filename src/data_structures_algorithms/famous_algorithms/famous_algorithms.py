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


def ae_dijkstras_algorithm(start: int, edges) -> List[int | float]:
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
    visited = set()
    def get_vertex_with_min_distance(distances: List[int|float] , visited: set):
        min_distance = float('inf')
        vertex = None

        for vertex_idx, distance in enumerate(distances):
            if vertex_idx in visited:
                continue
            if distance <= min_distance:
                vertex = vertex_idx
                min_distance = distance

        return vertex, min_distance
    

    while len(visited) != num_vertices:
        vertex, current_min_distance = get_vertex_with_min_distance(min_distances, visited)
        if current_min_distance == float('inf'):
            break
        visited.add(vertex)
        for destination, distance in edges[vertex]:
            if destination in visited:
                continue
            new_path_distance = current_min_distance + distance
            if new_path_distance < min_distances[destination]:
                min_distances[destination] = new_path_distance

    return list(map(lambda x: -1 if x == float('inf') else x, min_distances))




