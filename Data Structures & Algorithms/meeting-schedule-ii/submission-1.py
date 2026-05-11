"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        rooms = []
        currentConflicts = 0
        noRooms = 0
        last = None
        for i in range(len(intervals)):
            current = intervals[i]
            if last == None:
                rooms.append([current])
                last = current
                continue
            foundWhere = False
            for room in rooms:
                if room[-1].end <= current.start:
                    room.append(current)
                    foundWhere = True
                    break
            if not foundWhere:
                rooms.append([current])

        return len(rooms)
