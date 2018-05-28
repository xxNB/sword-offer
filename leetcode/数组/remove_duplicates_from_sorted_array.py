"""

100. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A == []:
            return 0
        index = 0
        for i in range(1, len(A)):
            if A[index] != A[i]:
                index += 1
                A[index] = A[i]

        return index + 1