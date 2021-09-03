# Link to video: https://youtu.be/U6Vz68sxidA

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s0, s1 = 0, 0
        g0, g1 = n - 1, n - 1
        
        if grid[0][0] == 1:
            return -1
        if n == 1:
            if grid[0][0] == 0:
                return 1
            return -1
        
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        seen = set()
        seen.add((0, 0))
        
        q = [(1, (0, 0))]
        
        while q:
            h = q.pop(0)
            a, b = h[1][0], h[1][1]
            if a == g0 and b == g1 and grid[g0][g1] == 0:
                return h[0]
            
            seen.add(h[1])
            for s in steps:
                c, d = a + s[0], b + s[1]
                if (c, d) in seen or not (0 <= c < n and 0 <= d < n) or grid[c][d] == 1:
                    continue
                seen.add((c, d))
                q.append((h[0] + 1, (c, d)))
        return -1
        