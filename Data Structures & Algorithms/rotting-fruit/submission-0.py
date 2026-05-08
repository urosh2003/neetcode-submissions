class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = 0
        toSpread = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten += 1
                    toSpread.append((i,j))

        def spreadRot(grid, i, j):
            newlyRotten = []
            if i > 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                newlyRotten.append((i-1, j))
            if j > 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                newlyRotten.append((i, j-1))
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                newlyRotten.append((i+1, j))
            if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                newlyRotten.append((i, j+1))

            return newlyRotten

        minutes = 0

        while fresh != 0 and toSpread:
            newlyRotten = []
            for i,j in toSpread:
                newlyRotten += spreadRot(grid, i, j)
            fresh -= len(newlyRotten)
            toSpread = newlyRotten
            minutes += 1


        if fresh!=0:
            return -1 

        return minutes               