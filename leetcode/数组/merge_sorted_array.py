class Solution:
    def mergeSorted(self, A, B):
        re = list()
        a, b =  0, 0
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                re.append( A[a])
                a += 1
            else:
                re.append(B[b])
                b += 1
        while a < len(A):
            re.append(A[a])
            a += 1
        while b < len(B):
            re.append(B[b])
            b += 1
        return re


r = Solution()
r.mergeSorted([1], [1])
