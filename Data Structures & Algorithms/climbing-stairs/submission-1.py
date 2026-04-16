class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        current = 1
        for i in range(n):
            nextt = prev + current
            prev = current
            current = nextt
        return current