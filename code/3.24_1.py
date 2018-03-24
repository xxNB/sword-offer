# -*- coding: utf-8 -*-

# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。


# *对vector容器内的数据进行排序，按照 将a和b转为string后
# 若 a＋b<b+a  a排在在前 的规则排序,
# 如 2 21 因为 212 < 221 所以 排序后为 21 2
#  to_string() 可以将int 转化为string

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        num = map(str, numbers)
        num.sort(lambda x, y: cmp(x + y, y + x))
        return ''.join(num)
