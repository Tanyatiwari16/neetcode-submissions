class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        Maxsum = nums[0]
        curr = nums[0]
        
        for i in range(1,len(nums)):

            if nums[i]< nums[i]+curr:
                
                curr+=nums[i]
                Maxsum=max(curr,Maxsum)
                
                
                
                
            else:
                Maxsum=max(Maxsum,nums[i])
                curr = nums[i]
                
        return Maxsum