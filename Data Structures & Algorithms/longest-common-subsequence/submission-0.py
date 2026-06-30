class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1  # Ensuring text1 is the longer one

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            prev = 0  # This stores dp[j-1] before it gets updated
            for j in range(1, len(text2) + 1):  # Start from index 1
                temp = dp[j]  # Store current dp[j] before modifying
                if text1[i] == text2[j - 1]:  # Since `text2` is 0-indexed
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])  # Use left value
                prev = temp  # Update prev for next iteration

        return dp[len(text2)]
