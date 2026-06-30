class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        Charset = set()
        res = 0
        for r in range(len(s)):
            while s[r] in Charset:
                Charset.remove(s[l])
                l+=1
            Charset.add(s[r])
            res = max(r-l+1,res)
        return res