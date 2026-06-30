class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)<len(text2):
            text1,text2 = text2,text1

        dp = [0]*(len(text2)+1)
        for i in range(len(text1)):
            diagonal = 0

            for j in range(1,len(text2)+1):
                temp = dp[j]
                if text1[i]==text2[j-1]:
                    dp[j] = diagonal+1
                else:
                    dp[j] = max(temp,dp[j-1])

                diagonal = temp

        return dp[-1]