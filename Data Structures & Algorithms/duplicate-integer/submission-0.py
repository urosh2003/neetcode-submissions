class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        br = {}
        for num in nums:
            if num in br:
                return True
            br[num] = True
        return False