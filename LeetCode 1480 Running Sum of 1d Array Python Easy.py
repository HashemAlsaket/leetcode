# Link to video: https://youtu.be/Yd5Q6S9LXAY

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        arr = []
        p = 0
        
        for num in nums:
            p += num
            arr.append(p)
    
        return arr