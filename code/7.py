# -*- coding: utf-8 -*-

# 定义栈的数据结构，在该类型中实现一个能够得到栈的最小元素的min函数

class Solution:
    def __init__(self):
        self.stack = []
        # 定义辅助栈，保持最后一个元素是最小的
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        # 如果栈底不相等，pop出的肯定不是最小的
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
