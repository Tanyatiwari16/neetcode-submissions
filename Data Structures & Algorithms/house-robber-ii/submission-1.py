class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def HR(nums):
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return max(nums[0],nums[1])
            one = nums[0]
            two = max(nums[0],nums[1])

            for i in range(2,len(nums)):
                temp = two
                two = max(two,nums[i]+one)
                one = temp
            return two
        if len(nums)==1:
            return nums[0]
        rob1 = HR(nums[1:])
        rob2 = HR(nums[:len(nums)-1])
        return max(rob1,rob2)