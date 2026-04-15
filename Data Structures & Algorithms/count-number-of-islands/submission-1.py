class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        islands = 0

        def visitNeighbors(i, j):
            if (i,j) in visited:
                return
            visited[(i,j)] = True

            if i > 0 and grid[i-1][j] == '1':
                visitNeighbors(i-1, j)
            if j > 0 and grid[i][j-1] == '1':
                visitNeighbors(i, j-1)
            if i < len(grid) - 1 and grid[i+1][j] == '1':
                visitNeighbors(i+1, j)
            if j < len(grid[i]) - 1 and grid[i][j+1] == '1':
                visitNeighbors(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == '1':
                    islands += 1
                    visitNeighbors(i, j)

        return islands