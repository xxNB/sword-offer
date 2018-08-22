class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_s = len(nums)
        if len_s == 0: return 0
        i , j= 0, 1
        while j < len_s:
            if nums[j]!=nums[i]:
                i+=1
                nums[i]= nums[j]
            j+=1
        return i+1



c= Solution()
c.removeDuplicates([1,1,2])
