# Link to video: https://www.youtube.com/watch?v=URsUV6CRLjA

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if nums.count(0) > 1:
            return [0] * n
        
        prod = 1
        for v in nums:
            if v != 0:
                prod = prod * v
        
        if nums.count(0) == 1:
            ans = [0] * n
            ind = nums.index(0)
            ans[ind] = prod
            return ans
        
        for i in range(n):
            nums[i] = prod // nums[i]
        return nums