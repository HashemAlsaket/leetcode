# Link to video: https://youtu.be/JNMJFbHPeXk

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        res = []
        left = intervals[0]
        for right in intervals:
            if right[0] <= left[1]:
                left = [min(left[0], right[0]), max(left[1], right[1])]
            else:
                res.append(left)
                left = right
        res.append(left)
        return res