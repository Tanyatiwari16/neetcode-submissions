class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        j = 0
        i = 1
        profit = 0
        while i<len(prices):
            if prices[i]<prices[j]:
                j=i
                i+=1
            else:
                profit = max(profit,prices[i]-prices[j])
                i+=1
        return profit
