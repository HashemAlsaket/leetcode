# Link to video: https://youtu.be/6chlRI3g__E

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                diff = abs(nums[i + 1] - nums[i])
                c += diff + 1
                nums[i + 1] += diff + 1
        return c