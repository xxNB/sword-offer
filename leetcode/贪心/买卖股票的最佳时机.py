class Solution:
    def maxProfit(self, prices):
        if prices==None or len(prices)==0:
            return 0
        Min = prices[0]
        res=0
        for p in prices:
            # 保存最大利益
            res = max(res,p-Min)
            # 寻找最小本钱
            Min = min(Min, p)
