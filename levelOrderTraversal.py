from collections import deque
from typing import List, Optional

DEBUG = True


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
    queue2 = deque()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Testing enqueue: ", enqueue(queue2, 10))
    print("Testing dequeue: ", dequeue(queue2))
    print("Testing enqueue: ", enqueue(queue2, 20))
    print("Testing peek: ", peek(queue2))

    print("----------------2-----------------")
    print("Testing level_order: ", level_order(root))

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print("----------------3-----------------")
    print("Testing return_bfs_traversal: ", return_bfs_traversal(graph, "A"))

    print(
        "----------------3-----------------\nTesting return_shortest_path: ",
        return_shortest_path(graph, "A", "F"),
    )
