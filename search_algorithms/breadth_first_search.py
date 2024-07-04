from collections import deque
from typing import List, Optional

DEBUG = False
TEST_BFS_TRAVERSAL = False
TEST_LEVEL_ORDER = False
TEST_RETURN_SHORTEST_PATH = False
TEST_SYMMETRY_CHECK = True
TEST_QUEUE_OPERATIONS = False


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


"""
This is the level-order/bfs traversal of a binary search tree. For trees, they mean the same thing. 
General notes: 
    -n nodes will take up a minimum of O(n/2) levels, so the runtime is O(n). 
    - popleft() is used for queues because they are first in first out. 
"""


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current_level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result


def symmetry_check(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    queue = deque([root])
    while queue:
        current_level = []
        for _ in range(len(queue)):  # taking out the elements in that level
            node = dequeue(queue)
            if node:
                current_level.append(node.val)
                enqueue(queue, node.left)
                enqueue(queue, node.right)
            else:
                current_level.append(None)
        l = 0
        r = len(current_level)-1
        while l < r:
            if current_level[l] != current_level[r]:
                return False
            l += 1
            r += -1
    return True


def enqueue(queue, element):
    queue.append(element)
    return queue


def dequeue(queue):
    if not queue:
        return None
    return queue.popleft()


def peek(queue):
    if not queue:
        return None
    return queue[0]


"""
This is a bfs for a graph traversal. Graph is a dictionary where each key (the node) is linked to a list of neighboring
nodes. 
"""


def return_bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = dequeue(queue)
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result


"""
Traverse through the graph and track the path, which will be the shortest path because this is BFS. 
"""


def return_shortest_path(graph: dict, start: str, target: str) -> List[str]:
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, shortest_path = dequeue(queue)

        if DEBUG:
            print("Popped off of stack: ", node, shortest_path)

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == target:
                    return shortest_path + [neighbor]
                else:
                    # concatenating lists with "+" creates a NEW COPY of the list.
                    new_path = shortest_path + [neighbor]
                    enqueue(queue, (neighbor, new_path))

                    if DEBUG:
                        print("new_path:", new_path)
    return []


if __name__ == "__main__":
    pass