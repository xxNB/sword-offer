"""
41. Maximum Subarray
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge
Can you do it in time complexity O(n)?
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, A):
        # write your code here
        curr_sum = 0
        max_sum = float('-inf')
        for i in range(len(A)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + A[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum
