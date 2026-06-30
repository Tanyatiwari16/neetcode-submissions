class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Hashset = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):

            while s[r] in Hashset:
                Hashset.remove(s[l])
                l+=1
            Hashset.add(s[r])
            maxlen = max(maxlen,len(Hashset))
        
        return maxlen