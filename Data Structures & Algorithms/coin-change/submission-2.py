class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(last, target):
            if (last,target) in cache:
                return cache[(last,target)]
            if target == 0:
                return 0
            if target < 0 or last < 0:
                return -1

            withLast = dfs(last, target - coins[last])
            withoutLast = dfs(last-1, target)
            if withLast > -1:
                if withoutLast > -1:
                    cache[(last,target)] = min(withLast+1, withoutLast)
                    return min(withLast+1, withoutLast)
                else:
                    cache[(last,target)] = withLast+1
                    return withLast+1
            else:
                cache[(last,target)] = withoutLast
                return withoutLast


        return dfs(len(coins)-1, amount)