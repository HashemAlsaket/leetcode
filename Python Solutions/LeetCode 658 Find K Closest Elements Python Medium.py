# Link to video: https://youtu.be/Lqx-edHekgw

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]
        
        def binsearch(arr, v):
            lo, hi = 0, len(arr) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == v:
                    return mid, mid
                if arr[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo, hi
        
        lo, hi = binsearch(arr, x)
        if abs(x - arr[lo]) < abs(x - arr[hi]):
            mid = lo
        else:
            mid = hi
        i, j = mid, mid
        k -= 1
        
        while k != 0:
            if i == 0:
                j += 1
            elif j == n - 1:
                i -= 1
            elif abs(x - arr[i - 1]) <= abs(x - arr[j + 1]):
                i -= 1
            else:
                j += 1
            k -= 1
        return arr[i:j + 1]
        