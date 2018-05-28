"""

479. Second Max of Array
Find the second max number in a given array.

Example
Given [1, 3, 2, 4], return 3.

Given [1, 2], return 1.
"""


class Solution:

    def secondMax(self, numbers):
        count = 0
        n1 = n2 = float('-inf')
        for x in numbers:
            count += 1
            if x > n2:
                if x >= n1:
                    n1, n2 = x, n1
                else:
                    n2 = x
        return n2 if count >= 2 else None



r = Solution()
r.secondMax([1, -1, -2])
