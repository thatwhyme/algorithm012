class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def conque(grid,i,j):
            if i<0 or i >=m or j<0 or j >=n or grid[i][j] !='1':
                return
            grid[i][j] = '0'
            conque(grid,i+1,j)
            conque(grid,i-1,j)
            conque(grid,i,j+1)
            conque(grid,i,j-1)
            
        landNum = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]== '1':
                    landNum += 1
                    conque(grid,i,j) 
        return landNum