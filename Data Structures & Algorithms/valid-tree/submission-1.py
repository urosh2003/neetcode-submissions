class Node:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = []

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        firstNode = None
        for pair in edges:
            num = pair[0]
            if num not in graph:
                graph[num] = Node(num)
            node = graph[num]
            if not firstNode:
                firstNode = node
            neighbor = pair[1]
            if neighbor not in graph:
                graph[neighbor] = Node(neighbor)
            neighborNode = graph[neighbor]
            node.neighbors.append(neighborNode)
            neighborNode.neighbors.append(node)

        if not firstNode:
            return True

        # moramo sve visited al ne smemo nikog visited dvaput
        visited = set()
        usedEdges = set()
        toVisit = [firstNode]
        while toVisit:
            current = toVisit.pop()
            if current in visited:
                return False
            visited.add(current)
            for neighbor in current.neighbors:
                if (neighbor.val, current.val) not in usedEdges:
                    usedEdges.add((current.val, neighbor.val))
                    toVisit.append(neighbor)

        return len(visited) == n





















