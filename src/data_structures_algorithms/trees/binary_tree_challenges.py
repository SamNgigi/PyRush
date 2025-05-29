from dataclasses import dataclass
from typing import Optional
from collections import deque

@dataclass
class Node:
    val: int = 0
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def bfs_tree_print(root: Optional['None']):
    """
    Given a tree return print the levels of the tree values

    Example

            1
          /   \
        2       3
      /       /   \\ 
    4       5       6



    Result
    1
    2 3
    4 5 6
    """
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_items = []

        for _ in range(level_size):
            cn = queue.popleft()
            if cn:
                level_items.append(cn.val)

                if cn.left:
                    queue.append(cn.left)
                if cn.right:
                    queue.append(cn.right)
        print(" ".join(level_items))
