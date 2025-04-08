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
