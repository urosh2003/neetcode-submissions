"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}
        toVisit = [node]
        if not node:
            return
        while toVisit:
            current = toVisit.pop()
            if current.val not in graph:
                newNode = Node(current.val)
                graph[current.val] = newNode
            currentNew = graph[current.val]
            for neighbor in current.neighbors:
                if neighbor.val not in graph:
                    newNode = Node(neighbor.val)
                    graph[neighbor.val] = newNode
                    toVisit.append(neighbor)
                newNeighbor = graph[neighbor.val]
                currentNew.neighbors.append(newNeighbor)

        return graph[1]