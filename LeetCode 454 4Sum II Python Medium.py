# Link to video: https://youtu.be/LDtB-m2jNHQ

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        da, db, dc, dd = {}, {}, {}, {}
        
        for v in A:
            if v not in da:
                da[v] = 0
            da[v] += 1
        for v in B:
            if v not in db:
                db[v] = 0
            db[v] += 1
        for v in C:
            if v not in dc:
                dc[v] = 0
            dc[v] += 1
        for v in D:
            if v not in dd:
                dd[v] = 0
            dd[v] += 1
        
        d1, d2 = {}, {}
        
        for k in da:
            for k2 in db:
                if k + k2 not in d1:
                    d1[k + k2] = da[k] * db[k2]
                else:
                    d1[k + k2] = d1[k + k2] + da[k] * db[k2]
        for k in dc:
            for k2 in dd:
                if k + k2 not in d2:
                    d2[k + k2] = dc[k] * dd[k2]
                else:
                    d2[k + k2] = d2[k + k2] + dc[k] * dd[k2]
        
        c = 0
        for k in d1:
            if 0 - k in d2:
                c += (d1[k] * d2[0 - k])
        return c
        