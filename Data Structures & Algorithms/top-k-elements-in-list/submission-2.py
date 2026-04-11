class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        res = []
        print(counts)
        for num in counts.keys():
            if len(res) == 0:
                res.append((num, counts[num]))
                continue
            for i in range(len(res)):
                if counts[num] >= res[i][1]:
                    res.insert(i, (num, counts[num]))
                    break
                elif i == len(res)-1:
                    res.append((num, counts[num]))
        
        final = []
        print(res)

        for i in range(k):
            final.append(res[i][0])

        return final