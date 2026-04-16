class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = [0] * len(nums)
        for i in range(0, len(nums)-1):
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

        best2 = [0] * len(nums)
        for i in range(len(nums)-1, 0, -1):
            prev = 0
            prevprev = 0
            if i < len(nums)-1:
                prev = best2[i+1]
            if i < len(nums)-2:
                prevprev = best2[i+2]

            if prevprev + nums[i] > prev:
                best2[i] = prevprev + nums[i]
            else:
                best2[i] = prev

        print(best)
        print(best2)

        return max(best[len(best)-2], best2[1])