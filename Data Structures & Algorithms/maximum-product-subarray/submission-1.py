class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        Max,Min = nums[0],nums[0]
        res = Max
        for i in range(1,len(nums)):
            curr = Max
            Max =  max(nums[i]*Max, nums[i]*Min,nums[i])
            Min = min(nums[i], Min*nums[i],curr*nums[i])
            res = max(res,Max)
        return res