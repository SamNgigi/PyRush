from typing import Any
from collections import deque

class AdjacencyMatrixGraph:
    """
    Represents a graph as a 2D matrix where matrix[i][j] represents an edge from i to j
    For unweighted graphs we use 1 (or True) to represent an edge and 0(or False) for no edge.
    For weighted graphs we store the weight instead of 1 and ofter use infinity or a special val to indicate no edge

    PROS:
    - O(1) lookup time to check if there's an edge between 2 vertices
    - Simple implementation for dense graphs
    - Good for algorithms that need to quickly check if two vertices are connected

    CONS:
    - O(V^2) space complexity regardless of the number of edges
    - Inefficient for sparse graphs (where E << V^2)
    """ 
    def __init__(self, num_vertices: int, directed: bool=False): # undirected graph by default
        self.num_vertices = num_vertices
        self.directed = directed
        
        # Initialize with zeros (no edges)
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)] # unweighted graph

    def invalid_range(self, source, dest) -> bool: 
        return source >= self.num_vertices or dest >= self.num_vertices or source < 0 or dest < 0

    def add_edge(self, source, dest, weight = 1) -> None:
        if self.invalid_range(source, dest):
            print("Vertex out of range")
            return
        
        self.matrix[source][dest] = weight
        if not self.directed: # If undirected add two way edge
            self.matrix[dest][source] = weight

    def remove_edge(self, source, dest) -> None:
        if self.invalid_range(source, dest):
            print("Vertex out of range")
            return
        
        self.matrix[source][dest] = 0
        if not self.directed:
            self.matrix[dest][source] = 0

    def has_edge(self, source, dest):
        if self.invalid_range(source, dest):
            return False
        return self.matrix[source][dest] != 0
    
    def get_neighbors(self, vertex) -> list:
        if vertex >= self.num_vertices or vertex < 0:
            print("Vertex out of range")
            return []
        neighbors = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] != 0:
                neighbors.append((i, self.matrix[vertex][i])) # appending (vertex, weight)
        return neighbors

    def print_graph(self):
        for i in range(self.num_vertices):
            row = [str(x) for x in self.matrix[i]]
            print(f"Vertex {i}: {' '.join(row)}")



class AdjacencyList:
    """
    This uses an array or hash table(dict) where each index or key represents a vertex,
    and he value is a list of the vertices connected to that vertex

    Pros:
    - Space efficient for sparse graphs (only stores the edges that exist)
    - Faster iteration over all edges
    - Better for most graph algorithms like BFS, DFS
    
    Cons:
    - Checking if an edge exists between 2 vertices takes O(E) in the worst case
    - Can be less efficient for dense graphs
    """

    def __init__(self, directed: bool= False):
        self.graph = {} # Using a graph to represent our Adjacency List
        self.directed = directed


    def add_vertex(self, vertex: Any):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source: Any, dest: Any, weight:int = 1):
        if source not in self.graph:
            self.add_vertex(source)
        if dest not in self.graph:
            self.add_vertex(dest)

        self.graph[source].append((dest, weight))

        if not self.directed:
            self.graph[dest].append((source, weight))
    
    def remove_edge(self, source: Any, dest: Any):

        if source not in self.graph or dest not in self.graph:
            print("Either source or destination not in graph")
            return
        
        self.graph[source] = [edge for edge in self.graph[source] if edge[0] != dest]

        if not self.directed:
            self.graph[dest] = [edge for edge in self.graph[dest] if edge[0] != source]
    
    def has_edge(self, source: Any, dest: Any):
        
        if source not in self.graph or dest not in self.graph:
            print("Either source or destination not in graph")
            return False
        return any(edge[0] == edge for edge in self.graph[source])
    
    def get_neighbours(self, vertex: Any) -> list:
        if vertex not in self.graph:
            print("Vertex not in graph")
            return []
        return self.graph[vertex]
    
    def bfs(self, start_vertex):
        """
        Performs BFS traversal on Adjacency List graph starting for start_vertex.

        Args:
            start_vertex: The vertex to start BFS from

        Returns:
            visited: Set of vertices that were visited
            parent: Dictionary mapping vertex to its parent in the BFS tree
            distance: Dictionary mapping vertex to its distance from start vertex
        """
        # Initialize data structures
        visited = set()
        queue = deque([start_vertex])
        parent = {start_vertex: None}
        distances = {start_vertex: 0}
        traversal_order = []

        visited.add(start_vertex)

        while queue:

            current = queue.popleft()
            traversal_order.append(current)

            # Process each neighbor of the current vertex
            for neighbor, _ in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current
                    distances[neighbor] = distances[current] + 1

        return visited, parent, distances, traversal_order

    def dfs_recursive(self, start_vertex):
        if start_vertex not in self.graph:
            print("Start Vertex not in graph")

        visited = set()


    def dfs_iterative(self, start_vertex):
        
        visited = set()
        stack = deque([start_vertex])
        parent = {start_vertex: None}
        distances = {start_vertex: 0}
        traversal_order = []
        

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                traversal_order.append(current)
                neighbors = self.graph.get(current, []) 
                for child, _ in neighbors:
                    if child not in visited:
                        stack.append(child)
                        if child not in parent:
                            parent[child] = current
                            distances[child] = distances[current] + 1

        return visited, parent, distances, traversal_order



    def print_graph(self)->None:

        for vertex, edges in self.graph.items():
            print(f"Vertex {vertex}: {edges}")


class EdgeList:
    """
    This representation is simply a list of all edges in a graph, usually stored in
    pairs or triplets (for weighted graphs)

    Pros
    - Simple to implement
    - Good for algorithms that process all edges sequentially
    - Memory efficient for sparse graphs

    Cons
    - Inefficient for checking if an edge exists of finding neighbors of a vertex
    - Most graph algorithms need to convert this to another representation first
    """

    def __init__(self, directed: bool = False):
        self.edges = []
        self.directed = directed
        self.vertices = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, source: Any, dest:Any, weight: int = 1):
        self.vertices.add(source)
        self.vertices.add(dest)
        self.edges.append((source, dest, weight))

        if not self.directed: # undirected graph
            self.edges.append((dest, source, weight))

    def remove_edge(self, source:Any, dest:Any):
        if source not in self.vertices or dest not in self.vertices:
            print("Either source on dest not in graph")
            return
        
        self.edges = [edge for edge in self.edges if not (edge[0] == source and edge[1] == dest)]
        if not self.directed:
            self.edge = [edge for edge in self.edges if not (edge[0] == dest and edge[1] == source)]
    
    def has_edge(self, source:Any, dest:Any)->bool:
        if source not in self.vertices or dest not in self.vertices:
            print("Either source or dest not in graph")
            return False
        return any(edge[0] == source and edge[1] == dest for edge in self.edges)
    
    def get_neighbours(self, vertex: Any) -> list:
        if vertex not in self.vertices:
            print("Vertex not in graph")
            return []
        
        neighbors: list = []
        for edge in self.edges:
            if edge[0] == vertex:
                neighbors.append((edge[1], edge[2])) # neighbor, weight for which vertex is source

            elif not self.directed and edge[1] == vertex:
                neighbors.append((edge[0], edge[2])) # neighbor, weight for which vertex is destination

        return neighbors

    def print_graph(self):
        print("Edges:")
        for edge in self.edges:
            print(f"{edge[0]} -> {edge[0]} (weight: {edge[2]})")
        print("Vertices:", self.vertices)



if __name__ == "__main__":

    sample_graph = [(0, 1, 2), (0, 3 , 1), (1, 2, 3), (3, 2, 1), (2, 4, 5), (3, 4, 4)]

    adj_list = AdjacencyList(directed=True)

    for src, dest, weight in sample_graph:
        adj_list.add_edge(source=src, dest=dest, weight=weight)

    adj_list.print_graph()
    print("-" * 40)
    print("BFS")
    print("-" * 40)
    _visited, _parent, _distance, _traversal = adj_list.bfs(0)
    print(f"Visited: {_visited}")
    print(f"parent: {_parent}")
    print(f"distance: {_distance}")
    print(f"traversal: {_traversal}")
    print("-"*40)
    visited_, parent_, distance_, traversal_ = adj_list.dfs_iterative(0)
    print("-" * 40)
    print("DFS")
    print("-" * 40)
    print(f"Visited: {visited_}")
    print(f"parent: {parent_}")
    print(f"distance: {distance_}")
    print(f"traversal: {traversal_}")

