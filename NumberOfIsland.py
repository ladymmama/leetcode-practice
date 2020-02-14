class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid: #check if empty
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.dfs(grid, r, c)
                    print(self.dfs(grid, r, c))
                    count += 1 #everytime we do dfs, we have an isaland
        return count
    
    def dfs(self, grid, i, j):
        dirs = [[-1,0], [0,1], [0,-1], [1,0]] #do dfs in all directions
        grid[i][j] = 0 #mark every visited 1 to 0 to avoid duplicaion
        for move in dirs:
            nr = i + move[0]
            nc = j + move[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]): #we should consider that row and colum shoould all less than the range and greater or equal to 0
                if grid[nr][nc] == 1: #do recursion until the whole island
                    self.dfs(grid, nr, nc)
