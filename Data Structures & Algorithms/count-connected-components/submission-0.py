class Node:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = []

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        firstNode = None
        res = 0
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
            return res

        res += n - len(graph)

        visited = set()
        exploring = set()
        explored = set()
        paths = set()

        def explore(node):
            if node in exploring:
                return

            exploring.add(node)
            for neighbor in node.neighbors:
                if neighbor in explored:
                    continue
                explore(neighbor)

            explored.add(node)

            return False



        toVisit = [firstNode]
        for node in graph.values():
            current = node
            if current not in explored:
                res += 1
                exploring = set()
                explore(current)



        return res