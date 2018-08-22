class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        一开始这个题目我没有想到能达到题目要求的算法，不过如果可以使用额外的数组空间的话可以用前面268.缺失数字中思路2的方法，但是这个不让用，
        后来才得到这个思路，就是不是用0,1来表示这个数有没有出现过，由于给定的数组全是正数，直接用数组中对应位置的数作为索引将对应索引的数变成
        相反数来表示有没有出现过该数，同时取索引的时候加一个绝对值，这样就不会丢失原数组中的数据啦，不然你把对应位置都置1了，那么这个位置
        的数就丢了啊。似不似。
        """
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index]>0:
                nums[index] = -nums[index]
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans

r = Solution()
print(r.findDisappearedNumbers([4,3,2,7,8,2,3,1]))