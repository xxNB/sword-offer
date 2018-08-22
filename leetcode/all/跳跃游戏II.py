"""
    贪心算法
"""

class Solution:
    def jump(self, A):
        n = len(A)
        cur, far = 0, 0
        step = 0
        far = A[0]
        while cur < n:
            if far >= n-1:
                return step + 1
            next_step = cur
            temp = far
            while cur <= temp:
                if A[cur] + cur > far:
                    next_step = cur
                    # 此时能跳到的最远位置为far
                    far = A[cur]+cur
                cur += 1
            step += 1
            cur = next_step