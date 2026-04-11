class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        current = 1
        for num in nums:
            l.append(current)
            current *= num
            

        r = []
        current = 1
        for i in range(len(nums)-1, -1, -1):
            r.insert(0,current)
            current *= nums[i]
            
        for i in range(len(r)):
            r[i] *= l[i]
        
        return r