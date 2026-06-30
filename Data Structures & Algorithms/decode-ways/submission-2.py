class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0:
            return 1

        prev2 = 1
        prev1 = 0 if s[0]=='0' else 1
        for i in range(2, len(s)+1):

            curr = 0
            one = int(s[i-1])
            two = int(s[i-2:i])

            if 1<=one<=9:
                curr = curr + prev1
            if 10<=two<=26:
                curr+=prev2
            
            prev2= prev1
            prev1 = curr

        return prev1