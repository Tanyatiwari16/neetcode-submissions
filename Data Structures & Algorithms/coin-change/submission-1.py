class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = amount
        dp = [float('inf')] * (total + 1)
        dp[0] = 0  # Base case: 0 coins needed to make sum 0

        # Process each coin type
        for coin in coins:
            for j in range(coin, total + 1):  # Start from coin value to avoid negative indices
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[total] if dp[total] != float('inf') else -1