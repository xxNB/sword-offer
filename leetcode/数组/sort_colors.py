"""
148. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

class Solution:
    def sort(self, A, flag, index):
        print("A, flag, index", A, flag, index)
        start, end = index, len(A) - 1
        while start <= end:
            while start <= end and A[start] == flag:
                print("start, end", start, end)
                start += 1
            while start <= end and A[end] != flag:
                end -= 1
            if start <= end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        # print("return start", start)
        return start

    def sortColors(self, A):
        self.sort(A, 1, self.sort(A, 0, 0))


r = Solution()
r.sortColors([1,0,1,2])