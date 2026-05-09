class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeLeft():
            i = len(intervals) - 1
            while i > 0:
                current = intervals[i]
                previous = intervals.pop(i-1)
                if previous[1] >= current[0]:
                    current[0] = min(current[0], previous[0])
                    current[1] = max(current[1], previous[1])
                    i -= 1
                else:
                    intervals.insert(i-1, previous)
                    break

        def mergeRight():
            i = 0
            while i < len(intervals) - 1:
                current = intervals[i]
                nextt = intervals.pop(i+1)
                if nextt[0] <= current[1]:
                    current[0] = min(current[0], nextt[0])
                    current[1] = max(current[1], nextt[1])
                else:
                    intervals.insert(i+1, nextt)
                    i += 1
            
        
        inserted = -1
        for i in range(len(intervals)-1):
            interval = intervals[i]
            intervalNext = intervals[i+1]
            if interval[0] <= newInterval[0] <= intervalNext[0]:
                intervals.insert(i+1, newInterval)
                inserted = i+1
                break

        if inserted == -1:
            if intervals and newInterval[0] < intervals[0][0]:
                intervals.insert(0, newInterval)
            else:
                intervals.append(newInterval)

        print(intervals)
        mergeRight()
        #mergeLeft()


        return intervals