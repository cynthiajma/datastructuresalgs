
from typing import List


class TreeNode:
	def __init__(self, value, left, right):
		self.val = value
		self.left = left
		self.right = right 



"""
This is a dfs iterative traversal for a graph. The TC is O(V+E), and the space is O(V) because of the stack. 
"""
def return_dfs_traversal(graph, start) -> list:
    visited = set()
    stack = [start]
    traversal_path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            traversal_path.append(vertex)
            visited.add(vertex)
            for neighbor in graph[vertex]:
            	if neighbor not in visited:
            		stack.append(neighbor)
    return traversal_path


    """
    This is a recursive dfs traversal that doesn't use a stack, but utilizes a call stack. Thus, the time complexity is O(V + E) or O(n). 
    The space complexity is O(n) because there is a list, and the call stack is O(V) in the worst case. 

    Algorithm usually uses recursion implementation. Also useful for finding connected components. 
    """

def recursive_dfs_traversal(graph, vertex, visited, result: List[TreeNode]): 
	if not visited:
		visited = set() 
	if not result:
		result = []
	else:
		visited.add(vertex)
		result.append(vertex)
	for neighbor in graph[start]:
		if neighbor not in visited:
			recursive_dfs_traversal(graph, neighbor, visited, result)
	return result




if __name__ == "__main__":
	pass


