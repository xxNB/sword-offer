# -*- coding: utf-8 -*-

# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数
# 序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快
# 的找出所有和为S的连续正数序列? Good Luck!

class Solution:
    def FindContinuousSequrnce(self, tsum):
            # write code here
        res = []
        for i in xrange(1, tsum / 2 + 1):
            for j in xrange(i, tsum / 2 + 2):
                # (上底加下底)乘高除以2
                tmp = (j + i) * (j - i + 1) / 2
                if tmp > tsum:
                    break
                elif tmp == tsum:
                    res.append(xrange(i, j + 1))
        return res
