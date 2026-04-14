class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        elem = nums.pop()
        subs = self.subsets(nums)
        startLen = len(subs)
        for i in range(startLen):
            subset = subs[i].copy()
            subset.append(elem)
            subs.append(subset)
        return subs