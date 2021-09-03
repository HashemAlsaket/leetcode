# Link to video: https://youtu.be/mzB9rTtFBy4

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def inside(p, cir):
            dist = (((p[0] - cir[0]) ** 2) + ((p[1] - cir[1]) ** 2)) ** 0.5
            return dist <= cir[2]
        
        res = []
        
        for cir in queries:
            c = 0
            for p in points:
                if inside(p, cir):
                    c += 1
            res.append(c)
        return res