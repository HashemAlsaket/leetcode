# Link to video: https://youtu.be/wx5PjUqFWDY

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums) - 1
        if hi == 0:
            return 0
        if hi == 1:
            if nums[0] > nums[1]:
                return 0
            return 1
        
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return hi
        
        if hi == 2:
            if nums[0] < nums[1] > nums[2]:
                return 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] >= nums[mid] >= nums[mid + 1]:
                hi = mid - 1
            else:
                lo = mid + 1
        