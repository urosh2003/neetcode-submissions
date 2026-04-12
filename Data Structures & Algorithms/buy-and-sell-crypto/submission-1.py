class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        buyp = prices[0]
        for i in range(1, len(prices)):
            buyp = min(buyp, prices[i])
            maxp = max(maxp, prices[i] - buyp)

        return maxp