class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        if n<=2:
            return n
        
        two = 2
        three = 3
        for i in range(3,n):
            temp = three
            three = three+two
            two = temp
        return three
            
