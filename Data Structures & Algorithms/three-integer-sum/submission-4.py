class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        targets = set()
        triples = []
        res = []
        nums.sort()
        left = 0
        right = len(nums) - 1

        for i in range(len(nums)):
            num = -nums[i]
            if num < 0:
                break

            if num in targets:
                continue

            target = num
            targets.add(num)

            left = i+1
            right = len(nums) - 1

            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                summ = nums[left] + nums[right]
                if summ == target:
                    print("Alo")
                    triple = [-target, nums[left], nums[right]]
                    triples.append(triple)
                    while left < right and nums[left] == triple[1]:
                        left += 1
                    while left < right and nums[right] == triple[2]:
                        right -= 1                        
                elif summ > target:
                    right -= 1
                elif summ < target:
                    left += 1
        
        return triples

        