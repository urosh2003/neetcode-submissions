class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = (left+right)//2

            num = nums[m]

            if left == right:
                return nums[m]
            elif nums[m] >= nums[right]:
                left = m+1
            elif nums[m] < nums[right]:
                right = m
