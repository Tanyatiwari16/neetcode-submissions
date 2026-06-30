class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
# Convert the dictionary to a set for O(1) lookups
        wordSet = set(wordDict)

        # Find the maximum word length in the dictionary
        maxLen = max(map(len, wordDict), default=0)

        n = len(s)
        # dp[i] states if the substring s[0..i] can be segmented
        dp = [False] * (n + 1)

        # Base case: empty string is valid
        dp[0] = True

        for i in range(1, n + 1):
            # Check prefixes of length up to maxLen
            for j in range(i - 1, max(0, i - maxLen) - 1, -1):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # Stop checking further prefixes

        return dp[n]

