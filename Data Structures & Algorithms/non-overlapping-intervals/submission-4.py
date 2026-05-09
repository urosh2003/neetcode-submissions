class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        

        def maxSize(i, previous) -> int:
            if i== len(intervals):
                return 0

            res = maxSize(i+1, previous)
            if previous == -1 or intervals[previous][1] <= intervals[i][0]:
                res = max(res, 1+maxSize(i+1, i))
            return res

        return len(intervals) - maxSize(0,-1)