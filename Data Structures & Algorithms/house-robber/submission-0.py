class Solution:
    def rob(self, nums: List[int]) -> int:
        best = [0] * len(nums)
        for i in range(len(nums)):
            prev = 0
            prevprev = 0
            if i > 0:
                prev = best[i-1]
            if i > 1:
                prevprev = best[i-2]

            if prevprev + nums[i] > prev:
                best[i] = prevprev + nums[i]
            else:
                best[i] = prev

        return best.pop()