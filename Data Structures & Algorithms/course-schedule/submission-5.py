class Node:
    def __init__(self, course, neighbors=[]):
        self.course = course
        self.neighbors = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        firstNode = None
        for pair in prerequisites:
            course = pair[0]
            if course not in graph:
                graph[course] = Node(course)
            node = graph[course]
            if not firstNode:
                firstNode = node
            required = pair[1]
            if required not in graph:
                graph[required] = Node(required)
            requiredNode = graph[required]
            node.neighbors.append(requiredNode)

        visited = set()
        exploring = set()
        explored = set()
        paths = set()

        def explore(node):
            if node in exploring:
                return True

            exploring.add(node)
            for neighbor in node.neighbors:
                if neighbor in explored:
                    continue
                cycle = explore(neighbor)
                if cycle:
                    return True

            explored.add(node)

            return False

        if not firstNode:
            
            return True
        print(firstNode.course)
        toVisit = [firstNode]
        for node in graph.values():
            current = node
            if current not in explored:
                exploring = set()
                cycle = explore(current)
                if cycle:
                    return False

        return True