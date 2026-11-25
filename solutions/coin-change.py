# LeetCode 322: Coin Change
# Student: Anurag Banik (Roll: 2026ABES042)
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    print('Coin Change Test:', s.coinChange([1, 2, 5], 11)) # Expected: 3
