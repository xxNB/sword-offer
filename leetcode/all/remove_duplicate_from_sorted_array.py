class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        j = 0
        n = len(A)
        for i in range(1, n):
            # 相等的话i的坐标继续增加
            if A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1
        return j + 1


r = Solution()
print(r.removeDuplicates([1, 1, 3, 4, 5, 5, 6, 7,]))
