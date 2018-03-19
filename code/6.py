# -*- coding: utf-8 -*-

# 输入一个矩阵，按照从外到里以顺时针依次打印出每一个数字。

class Solution:
    def printMatrix(self, matrix):
        result = []
        while matrix:
            # 取出第一行
            result = result + matrix.pop()
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        B = []
        for i in range(r):
            A = []
            for j in range(c):
                A.append(matrix[j][i])
            B.append(A)
        # 倒置剩下的矩阵
        B.reverse()
        return B

