class Solution:
    def sort(self, A, flag, index):
        print("A, flag, index", A, flag, index)
        start, end = index, len(A) - 1
        while start <= end:
            while start <= end and A[start] == flag:
                start += 1
            while start <= end and A[end] != flag:
                end -= 1
            if start <= end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        print("return start", start)
        return start

    def sortColors(self, A):
        self.sort(A, 1, self.sort(A, 0, 0))


r = Solution()
r.sortColors([1,0,1,2])