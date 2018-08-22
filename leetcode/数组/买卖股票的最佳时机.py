class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) ==0:
            return 0

        Min = prices[0]
        res =0
        for p in prices:
            res = max(res, p-Min)
            Min = min(Min, p)
        return res
