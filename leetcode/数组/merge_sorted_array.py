"""
6. Merge Two Sorted Arrays
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
"""


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
