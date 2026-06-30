class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = amount
        n = len(coins)
        dp = [[float('inf')] * (total + 1) for _ in range(n + 1)]

        # Base case: If sum is 0, no coins are needed
        for i in range(n + 1):
            dp[i][0] = 0  

        # Forward iteration over coins
        for i in range(1, n + 1):
            for j in range(1, total + 1):
                # Case 1: Not taking the current coin
                dp[i][j] = dp[i - 1][j]

                # Case 2: Taking the current coin (if possible)
                if j >= coins[i - 1] and dp[i][j - coins[i - 1]] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)

        return dp[n][total] if dp[n][total] != float('inf') else -1