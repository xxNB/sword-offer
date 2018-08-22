class Solution:
    def minCostClimbingStairs(self, cost):
        """
        dp[i] = min(dp[i- 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        动态规划： 动态规划表面上很难，其实存在很简单的套路：当求解的问题满足以下两个条件时， 就应该使用动态规划：
        主问题的答案 包含了 可分解的子问题答案 （也就是说，问题可以被递归的思想求解）
        递归求解时， 很多子问题的答案会被多次重复利用
        动态规划的本质思想就是递归， 但如果直接应用递归方法， 子问题的答案会被重复计算产生浪费， 同时递归更加耗费栈内存，
        所以通常用一个二维矩阵（表格）来表示不同子问题的答案， 以实现更加高效的求解
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0 for col in range(n+1)]
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[-1]

c= Solution()
print(c.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))