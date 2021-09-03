# Link to video: https://youtu.be/EB3rFH21-jo

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        
        for l in s:
            if l not in ds:
                ds[l] = 0
            ds[l] += 1
        for l in t:
            if l not in dt:
                dt[l] = 0
            dt[l] += 1
        
        if ds.keys() != dt.keys():
            return False
        
        for k in ds:
            if ds[k] != dt[k]:
                return False
        return True
        