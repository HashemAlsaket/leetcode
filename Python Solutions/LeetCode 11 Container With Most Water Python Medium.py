# Link to video: https://youtu.be/DT4o6mkq_r0

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height) - 1
        
        mx = 0
        
        while i < j:
            h1, h2 = height[i], height[j]
            mx = max(mx, min(h1, h2) * (j - i))
            if h1 < h2:
                i += 1
            else:
                j -= 1
        return mx
        
            