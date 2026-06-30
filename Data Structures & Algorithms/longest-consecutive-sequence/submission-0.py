class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Res = 0
        lookup = set(nums)
        for i in range(len(nums)):
            
            if nums[i] -1 not in lookup:
                cur = 0
                while nums[i]+cur in lookup:
                    cur+=1
                Res = max(Res,cur)

        return Res