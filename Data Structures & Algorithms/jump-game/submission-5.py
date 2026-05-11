class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = len(nums)-1
        while True:
            distance = nums[start]

            if start+distance >= end:
                return True
            if distance == 0:
                return False
            

            bestDistance = 0
            bestJump = 0
            for i in range(1, distance+1, 1):
                potential = i + nums[start+i]
                if potential >= bestDistance:
                    bestJump = i
                    bestDistance = potential
            start += bestJump

        return True

