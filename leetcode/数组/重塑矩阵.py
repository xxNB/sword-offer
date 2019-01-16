class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        reshape() ! 并非转置
        """
        h, w = len(nums), len(nums[0])
        if h * w != r * c: return nums
        ans = []
        p = q = 0
        for x in range(r):
            row = []
            for y in range(c):
                row.append(nums[p][q])
                #
                q += 1
                if q == w:
                    p += 1
                    q = 0
            ans.append(row)
        return ans
