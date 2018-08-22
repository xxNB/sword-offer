class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0:
            return []
        r, c = len(A), len(A[0])
        # 先for c 后 for r, 把列的所有数据拿到行里
        return [[A[i][j] for i in range(r)] for j in range(c)]


r = Solution()
print(r.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
