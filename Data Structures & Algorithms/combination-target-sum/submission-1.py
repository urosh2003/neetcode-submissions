class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target <= 0:
            return []
        if not nums:
            return []

        combinations = []
        for i in range(len(nums)):
            elem = nums[i]
            without = nums.copy()
            without.pop(i)

            if target == elem:
                combinations.append([elem])
            elif elem > target:
                continue
            else:
                combinations1 = self.combinationSum(nums[i:], target-elem)

                for combination in combinations1:
                    if combination:
                        combination.append(elem)
                        combinations.append(combination)


        return combinations
        

            