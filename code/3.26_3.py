# -*- coding: utf-8 -*-

# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串
# abc,acb,bac,bca,cab和cba。

import itertools
class Solution:
    def Permutation(self, ss):
        if not ss:
            return ss
        result = map(lambda x: ''.join(x), itertools.permutations(ss))
        result = list(set(result))
        # result.sort()
        return result



c = Solution()
print c.Permutation('abc')
