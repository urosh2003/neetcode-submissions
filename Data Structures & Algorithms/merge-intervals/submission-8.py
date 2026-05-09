class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        numbers = {}
        for interval in intervals:
            if interval[0] not in numbers:
                numbers[interval[0]] = 0
            if interval[1] not in numbers:
                numbers[interval[1]] = 0

            numbers[interval[0]] += 1
            numbers[interval[1]] -= 1

        current = None
        active = 0
        for num in sorted(numbers):
            if not current and numbers[num] > 0:
                current= [num, num]
                active += numbers[num]
                continue
            if numbers[num] < 0:
                current[1] = num
                active += numbers[num]
                if active == 0:
                    result.append(current)
                    current = None
            if numbers[num] > 0:
                active += numbers[num]
            if numbers[num] == 0:
                if active == 0:
                    result.append([num,num])
 
        return result  
        

        """
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
        """