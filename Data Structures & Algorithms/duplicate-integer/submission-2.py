class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        br = set()
        for num in nums:
            if num in br:
                return True
            br.add(num)
        return False