class Node:
    def __init__(self, height, i,j,pacific=False, atlantic=False):
        self.height = height
        self.pacific = pacific
        self.atlantic = atlantic
        self.lowerThan = []
        self.i = i
        self.j = j

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        graph = {}
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i,j) not in graph:
                    graph[(i, j)] = Node(heights[i][j], i,j)
                node = graph[(i, j)]
                if i == 0 or j == 0:
                    node.pacific = True
                if i == len(heights) - 1 or j == len(heights[i]) - 1:
                    node.atlantic = True

                if i > 0:
                    if heights[i][j] <= heights[i-1][j]: 
                        if (i-1, j) not in graph:
                            graph[(i-1, j)] = Node(heights[i-1][j], i-1,j)
                        node.lowerThan.append(graph[(i-1, j)])
                if j > 0:
                    if heights[i][j] <= heights[i][j-1]: 
                        if (i, j) not in graph:
                            graph[(i, j-1)] = Node(heights[i][j-1], i,j-1)
                        node.lowerThan.append(graph[(i, j-1)])
                if i < len(heights) - 1:
                    if heights[i][j] <= heights[i+1][j]: 
                        if (i+1, j) not in graph:
                            graph[(i+1, j)] = Node(heights[i+1][j], i+1,j)
                        node.lowerThan.append(graph[(i+1, j)])
                if j < len(heights[i]) - 1:
                    if heights[i][j] <= heights[i][j+1]: 
                        if (i, j+1) not in graph:
                            graph[(i, j+1)] = Node(heights[i][j+1], i,j+1)
                        node.lowerThan.append(graph[(i, j+1)])

        hasPacific = set()
        hasAtlantic = set()
        hasBoth = set()
        result = []
        def spread(node):
            if node not in hasPacific:
                if node.pacific:
                    hasPacific.add(node)
                    for neighbor in node.lowerThan:
                        neighbor.pacific = True   
                        spread(neighbor)    
                    if node.atlantic:
                        hasBoth.add(node) 

            if node not in hasAtlantic:  
                if node.atlantic:
                    hasAtlantic.add(node)
                    for neighbor in node.lowerThan:
                        neighbor.atlantic = True
                        spread(neighbor)
                    if node.pacific:
                        hasBoth.add(node)


        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if graph[(i, j)].atlantic and graph[(i, j)] not in hasAtlantic:
                    spread(graph[(i, j)])
                if graph[(i, j)].pacific and graph[(i, j)] not in hasPacific:
                    spread(graph[(i, j)])

        for node in hasBoth:
            result.append([node.i, node.j])

        return result