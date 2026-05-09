class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda i: i[0])
        
        for interval in intervals:
            if not result:
                result.append(interval)
                lastEnd = interval[1]
                continue
            if interval[0] <= lastEnd:
                result[-1][1] = max(interval[1], lastEnd)
                lastEnd = result[-1][1]
            else:
                result.append(interval)
                lastEnd = interval[1]

        return result  