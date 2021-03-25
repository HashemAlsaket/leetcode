# Link to video: https://youtu.be/4p50S6mMRrE

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        num_dict = {}
        
        for i in range(n):
            val = nums[i]
            num_dict[val] = num_dict.get(val, i)
            diff = target - val
            found_index = num_dict.get(diff, -1)
            if found_index != i and found_index != -1:
                return [i, found_index]