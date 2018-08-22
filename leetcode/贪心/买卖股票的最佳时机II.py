class Solution:
    def maxProfit(self,prices):
        profit = 0
        i=1
        while i<len(prices):
            diff = prices[i]-prices[i-1]
            if diff>0:
                profit+=diff
            i+=1
        return profit