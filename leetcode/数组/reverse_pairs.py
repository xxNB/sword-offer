"""
532. Reverse Pairs
For an array A, if i < j, and A [i] > A [j], called (A [i], A [j]) is a reverse pair.
return total of reverse pairs in A.

Example
Given A = [2, 4, 1, 3, 5] , (2, 1), (4, 1), (4, 3) are reverse pairs. return 3
"""
class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        # Write your code here
        self.tmp = [0] * len(A)
        return self.mergeSort(A, 0, len(A) - 1)

    def mergeSort(self, A, l, r):
        if l >= r:
            return 0
        print("l+r", l+r)
        m = (l + r) // 2
        print(m)
        ans = self.mergeSort(A, l, m) + self.mergeSort(A, m + 1, r)
        i, j, k = l, m + 1, l
        while i <= m and j <= r:
            if A[i] > A[j]:
                self.tmp[k] = A[j]
                j += 1
                ans += m - i + 1
            else:
                self.tmp[k] = A[i]
                i += 1
            k += 1

        while i <= m:
            self.tmp[k] = A[i]
            k += 1
            i += 1
        while j <= r:
            self.tmp[k] = A[j]
            k += 1
            j += 1
        for i in range(l, r + 1):
            A[i] = self.tmp[i]

        return ans

c = Solution()
c.reversePairs([2, 4, 1, 3, 5])