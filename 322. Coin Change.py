# 322. Coin Change
# Time: O(amount*len(coins))
# Space: O(amount)

# basic dp: dp[i] = minimum number of coins that needs to make up amount i
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a-c] + 1)

        return -1 if dp[amount] > amount else dp[amount]
