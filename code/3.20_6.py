# -*- coding: utf-8 -*-

# 输入俩个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序

class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or len(pushV) != len(popV):
            return False
        # 借助一个辅助栈
        stack = []
        for i in pushV:
            stack.append(i)
            # print(stack)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
                print(stack)
        # 如果弹出不一致，必然遗留
        if len(stack):
            return False
        return True 

r = Solution()
print(r.IsPopOrder([1,2,3,4,5], [5,4,2,3,1]))