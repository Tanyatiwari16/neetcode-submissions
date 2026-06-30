from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = amount
        n = len(coins)

        # Initialize dp matrix efficiently
        dp = [[0] * (total + 1) for _ in range(n + 1)]
        
        # First row: Cannot make any amount without coins
        for j in range(1, total + 1):
            dp[0][j] = float('inf')

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, total + 1):
                dp[i][j] = dp[i - 1][j]  # Case 1: Not using the coin
                if j >= coins[i - 1] and dp[i][j - coins[i - 1]] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)

        return dp[n][total] if dp[n][total] != float('inf') else -1
