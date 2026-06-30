class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #initilly goal is at last index
        goal = len(nums) -1
        prev = len(nums)-2

        while prev>=0:
            if nums[prev] + prev>= goal:
                goal = prev
                # prev-=1
            prev-=1
        return goal==0
        