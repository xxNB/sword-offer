class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 0
        if n ==1:
            return 1
        cnt = 1
        i = 1
        # re = nums[0]
        max_cnt = 0
        for re in nums:
            if i < n:
                if nums[i] > re:
                    cnt += 1
                else:

                    cnt = 1
                # re = nums[i]
                max_cnt = max(max_cnt, cnt)
                i += 1
        return max_cnt


c = Solution()
print(c.findLengthOfLCIS([1, 3, 5, 4, 7]))
