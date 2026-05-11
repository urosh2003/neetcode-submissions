class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxSum = -1e9
        for i in range(len(nums)):
            if summ < 0:
                newsumm = nums[i]
            else: 
                newsumm = summ+nums[i]
            maxSum = max(maxSum, newsumm)
            summ = newsumm

        return maxSum