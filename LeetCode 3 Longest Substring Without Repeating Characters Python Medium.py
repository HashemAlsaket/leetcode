# Link to video: https://www.youtube.com/watch?v=fcNWzbIPObI

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        
        d = {}
        mx = 0
        i, j = 0, 0
        
        while i < n and j < n:
            l = s[j]
            if d.get(l, 0) == 0:
                d[l] = 1
                j += 1
                continue
            mx = max(mx, j - i)
            while d[l] == 1:
                d[s[i]] -= 1
                i += 1
        mx = max(mx, j - i)
        return mx
        
        
        
        