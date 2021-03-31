# Link to video: https://www.youtube.com/watch?v=Xsd6KYvgRbA

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        
        # set starting index
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        
        # mark even or odd
        if (m + n) % 2 == 0:
            even_or_odd = 'even'
        else:
            even_or_odd = 'odd'
        
        # merge values from arrays until
        # you have middle value(s) for 
        # median
        while i < m and j < n:
            a, b = nums1[i], nums2[j]
            if a < b:
                i += 1
                arr.append(a)
            else:
                j += 1
                arr.append(b)
            if i + j == ((m + n) // 2) + 1:
                break
        
        # in case len(nums1) > len(nums2)
        while i < m:
            if i + j == ((m + n) // 2) + 1:
                break
            arr.append(nums1[i])
            i += 1
        
        # in case len(nums2) > len(nums1)
        while j < n:
            if i + j == ((m + n) // 2) + 1:
                break
            arr.append(nums2[j])
            j += 1
        
        # return median based on even or odd length
        if even_or_odd == 'even' and i + j == ((m + n) // 2) + 1:
            return (arr[-1] + arr[-2]) / 2
        else:
            return arr[-1]