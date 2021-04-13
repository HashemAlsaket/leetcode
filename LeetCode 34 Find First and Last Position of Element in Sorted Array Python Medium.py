# Link to video: https://youtu.be/KgC0n3ma2do

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        def binsearch(arr, v):
            lo, hi = 0, len(arr) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == v:
                    return mid
                if arr[mid] < v:
                    lo = mid + 1
                if arr[mid] > v:
                    hi = mid - 1
                mid = (lo + hi) // 2
            return -1
        
        i = binsearch(nums, target)
        if i == -1:
            return [-1, -1]
        j, k = i, i
        
        while j >= 0:
            if nums[j] != target:
                break
            j -= 1
        while k < n:
            if nums[k] != target:
                break
            k += 1
        
        j += 1
        k -= 1
        
        return [j, k]
        
        