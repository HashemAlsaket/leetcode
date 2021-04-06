# Link to video: https://youtu.be/7FdOx0ZNezo

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        d = {}
        m, n = len(grid), len(grid[0])
        
        def land_size(i, j, k):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            d[k] = d.get(k, 0) + 1
            
            land_size(i, j - 1, k)
            land_size(i, j + 1, k)
            land_size(i - 1, j, k)
            land_size(i + 1, j, k)
            
        
        for i in range(m):
            for j in range(n):
                k = (i, j)
                if grid[i][j] == 1:
                    land_size(i, j, k)
        
        if not d:
            return 0
        return max(d[k] for k in d)