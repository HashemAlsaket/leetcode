# Link to video: https://youtu.be/4SjxUqG2WZU

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        steps = [(2, -1), (1, -2), (-1, -2), (-2, -1), (-1, 2), (1, 2), (2, 1), (-2, 1)]
        seen = set()
        
        q = [(0, [0, 0])]
        
        while q:
            moves, coords = q.pop(0)
            if coords[0] == x and coords[1] == y:
                return moves
            
            for s in steps:
                nxtc = (coords[0] + s[0], coords[1] + s[1])
                
                if not ((nxtc[0] >= -2 and x >= -2
                        and nxtc[1] >= -2 and y >= -2) or
                        
                       (nxtc[0] <= 2 and x <= 2
                        and nxtc[1] <= 2 and y <= 2) or
                        
                       (nxtc[0] >= -2 and x >= -2
                        and nxtc[1] <= 2 and y <= 2) or
                        
                       (nxtc[0] <= 2 and x <= 2
                        and nxtc[1] >= -2 and y >= -2)):
                    continue
                
                if nxtc not in seen:
                    q.append((moves + 1, nxtc))
                    seen.add(nxtc)
            