class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        Sum = nums[0]
        for i in range(1,len(nums)):
            if Sum+nums[i]>nums[i]:
                Sum+=nums[i]
                res = max(Sum,res)
            else:
                Sum = nums[i]
                res = max(Sum,res)

        return res