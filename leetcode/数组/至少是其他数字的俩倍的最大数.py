class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[1]:
            max_num, sec_num = nums[1], nums[0]
            max_index =1
        else:
            max_num, sec_num = nums[0], nums[1]
            max_index = 0
        for ix, i in enumerate(nums[2:]):
            if max_num>i >sec_num:
                sec_num = i
            elif i>max_num:
                temp = max_num
                max_num=i
                sec_num = temp
                max_index = ix+2

        if max_num < sec_num*2:
            return -1
        return max_index

c = Solution()
print(c.dominantIndex([0,0,0,1]))