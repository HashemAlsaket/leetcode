# Link to video: https://youtu.be/c4_ZUkmCB_o

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        mx = nums[0]
        rs = 0
        
        for v in nums:
            mx = max(mx, rs)
            if rs <= 0:
                rs = v
                continue
            rs += v
        mx = max(mx, rs)
        if mx == 0:
            return max(nums)
        return mx
        