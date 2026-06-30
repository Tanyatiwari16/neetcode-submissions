class Solution:
    def findMin(self, nums: List[int]) -> int:

         
        l =  0

        r = len(nums) - 1
        Minterm = nums[l]
        while l<=r:

            if nums[l] <= nums[r]:
                Minterm = min(Minterm,nums[l])
                break

            m = (l+r)//2
            Minterm = min(Minterm,nums[m])
            if nums[m]<nums[l]:
                r = m-1
            else:
                l = m+1

        return Minterm