from typing import List, Union, Optional
from collections import deque
from sys import maxsize



def num_islands_med(grid: List[List[str]]) -> int:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

     

    Example 1:

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1
    Example 2:

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

    Args: 2D Matrix of strings

    Returns: int - number of islands
    """
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    island_count:int = 0
    neighbor_coords = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up ,down, left, right

    def dfs_recursive(row: int, col: int):
        if(row < 0 or col < 0 or row>=rows or col>= cols or grid[row][col] == "0"):
            return # invalid position
        
        grid[row][col] = "0" # instead of using visited
        for dr, dc in neighbor_coords:
            dfs_recursive((row+dr),(col+dc))

    def dfs_iterative(row: int, col: int):

        stack = deque([(row, col)])

        while stack:

            cr, cc = stack.pop()
            grid[cr][cc] = "0"

            for dr, dc in neighbor_coords:
                nr, nc = (cr + dr), (cc + dc)
                if(nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"): # or (nr, nc) not in visited
                    continue
                grid[nr][nc] = "0" # visited.add((nr, nc))
                stack.append((nr, nc))

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = "0" # instead of using a visited set i.e visited.add((r, c))

        while queue:
            cr, cc = queue.popleft()
            for dr, dc in neighbor_coords:
                nr, nc = dr + cr, dc + cc 
                if(nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                    continue
                queue.append((nr, nc))
                grid[nr][nc] = "0"
        

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs_recursive(r, c)
                island_count += 1

    


    return island_count



def can_visit_all_rooms_med(rooms: List[List[int]])->bool:
    """
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

     

    Example 1:

    Input: rooms = [[1],[2],[3],[]]
    Output: true
    Explanation: 
    We visit room 0 and pick up key 1.
    We then visit room 1 and pick up key 2.
    We then visit room 2 and pick up key 3.
    We then visit room 3.
    Since we were able to visit every room, we return true.
    Example 2:

    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
     

    Constraints:

    n == rooms.length
    2 <= n <= 1000
    0 <= rooms[i].length <= 1000
    1 <= sum(rooms[i].length) <= 3000
    0 <= rooms[i][j] < n
    All the values of rooms[i] are unique.

    Args: rooms List[List[int]]
    """

    stack = deque([0])
    visited = {0}
    
    while stack:
        current = stack.pop()

        for key in rooms[current]:
            if key not in visited:
                stack.append(key)
                visited.add(key)

    return len(rooms) == len(visited)

def flood_fill_ez(image: List[List[int]], sr: int, sc: int, color: int)->List[List[int]]:
    """
    You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill:

    Begin with the starting pixel and change its color to color.
    Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
    Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
    The process stops when there are no more adjacent pixels of the original color to update.
    Return the modified image after performing the flood fill.

     

    Example 1:

    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

    Output: [[2,2,2],[2,2,0],[2,0,1]]

    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

    Output: [[0,0,0],[0,0,0]]
    """
    if image[sr][sc] == color:
        return image
    
    original_color: int = image[sr][sc]
    ROWS, COLS = len(image), len(image[0])
    neighbor_coords: List[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
    queue: deque[tuple[int, int]] = deque([(sr, sc)])
    image[sr][sc] = color

    while queue:
        cr, cc = queue.popleft()
        for dr, dc in neighbor_coords:
            nr, nc = (cr + dr), (cc + dc)
            if(nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or image[nr][nc] != original_color):
                continue
            image[nr][nc] = color
            queue.append((nr, nc))
    return image

def nearest_0_matrix_med(mat: List[List[Union[int , str]]]) -> List[List[Union[int, str]]]:
    """
    Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

    The distance between two cells sharing a common edge is 1.

     

    Example 1:


    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]

    Example 2:


    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
 
    """
    neighbor_coords: List[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ROWS, COLS = len(mat), len(mat[0])
    queue = deque([])

    for row in range(ROWS):
        for col in range(COLS):
            if mat[row][col] == 0:
                queue.append((row, col))
            else:
                mat[row][col] = maxsize
    while queue:
        cr, cc = queue.popleft()

        for dr, dc in neighbor_coords:
            nr, nc = cr + dr, cc + dc
            if(0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == maxsize):
                mat[nr][nc] = mat[cr][cc] + 1
                queue.append((nr, nc))


    return mat

class LeetNode:

    def __init__(self, val:int = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



def copy_graph_med(node: Optional["LeetNode"]) -> Optional["LeetNode"]:
    if node is None:
        return None
    copy_map_dfs = {}
    copy_map_bfs = {}

    def bfs(node: "LeetNode") -> "LeetNode":
        
        copy_map_bfs[node] = LeetNode(node.val)
        queue = deque([node])

        while queue:

            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in copy_map_bfs:
                    copy_map_bfs[neighbor] = LeetNode(neighbor.val)
                    queue.append(neighbor)
                copy_map_bfs[current].neighbors.append(copy_map_bfs[neighbor])

        return copy_map_bfs[node]
    
    def dfs_recursive(node: "LeetNode") -> "LeetNode":
        if node in copy_map_dfs:
            return copy_map_dfs[node]

        node_copy = LeetNode(node.val)
        copy_map_dfs[node] = node_copy

        for neighbor in node.neighbors:
            node_copy.neighbors.append(dfs_recursive(neighbor))
        return node_copy

    

    bfs_result = bfs(node)
    dfs_result = dfs_recursive(node)

    return bfs_result

def can_finish_course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

     

    Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
    Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
     

    Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
    """
    course_preReq_graph = {i:[] for i in range(numCourses)}
    
    for crs, preReq in prerequisites:
        course_preReq_graph[crs].append(preReq)

    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        if course_preReq_graph[crs] == []:
            return True
        
        visited.add(crs)
        for preReq in course_preReq_graph[crs]:
            if not dfs(preReq): return False
        visited.remove(crs)
        course_preReq_graph[crs] = []
        return True
    
    for i in range(numCourses):
        if not dfs(i): return False
    
    return True


def rotten_oranges_med(grid: List[List[int]]) -> int:
    """
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

     

    Example 1:


    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
    Example 2:

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    Example 3:

    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
     

    Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
    """
    EMPTY, FRESH, ROTTEN = 0, 1, 2
    ROWS, COLS = len(grid), len(grid[0])
    neighbor_coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    fresh_count = 0
    queue = deque()

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == ROTTEN: # Our bfs starts from rotten oranges
                queue.append((row, col))
            if grid[row][col] == FRESH:
                fresh_count += 1
    if fresh_count == 0: return 0
    if not queue: return -1

    min_minutes = 0

    # Multi-source BFS
    while queue and fresh_count > 0:
        for _ in range(len(queue)):
            cr, cc = queue.popleft()
            for ncr, ncc in neighbor_coords:
                nr, nc = ncr + cr, ncc + cc
                if(0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                    grid[nr][nc] = ROTTEN
                    fresh_count -= 1
                    queue.append((nr, nc))
        min_minutes += 1

    return min_minutes if fresh_count == 0 else -1


def shortest_path_to_get_food_med():
    """
    You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

    You are given an m x n character matrix, grid, of these different types of cells:

    '*' is your location. There is exactly one '*' cell.
    '#' is a food cell. There may be multiple food cells.
    'O' is free space, and you can travel through these cells.
    'X' is an obstacle, and you cannot travel through these cells.
    You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

    Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

    Link to the original problem

    Example 1

    img1

    Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
    Output: 3
    Explanation: It takes 3 steps to reach the food.
    Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[row][col] is '*', 'X', 'O', or '#'.
    The grid contains exactly one '*'.
    """

    pass


if __name__ == "__main__":
    pass
