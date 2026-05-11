class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = len(nums)-1
        lastConsidered = 0
        while True:
            distance = nums[start]

            if start+distance >= end:
                return True
            if distance == 0:
                return False

            bestDistance = 0
            bestJump = 0
            for i in range(lastConsidered+1, start+distance+1, 1):
                potential = i + nums[i]
                if potential >= bestDistance:
                    bestJump = i
                    bestDistance = potential

            lastConsidered = start + distance
            start = bestJump

        return True

