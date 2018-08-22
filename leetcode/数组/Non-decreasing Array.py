"""
判断修改那个数字其实跟再前面一个数的大小有关系，首先如果再前面的数不存在，比如例子1，4前面没有数字了，
我们直接修改前面的数字为当前的数字2即可。而当再前面的数字存在，并且小于当前数时，比如例子2，-1小于2，
我们还是需要修改前面的数字4为当前数字2；如果再前面的数大于当前数，比如例子3，3大于2，
我们需要修改当前数2为前面的数3。这是修改的情况，
"""
class Solution:
    def checkPossibility(self, nums):
        if len(nums)<=2:
            return True
        count=0 if nums[0] <=nums[1] else 1
        for i in range(2, len(nums)):
            if nums[i-1] > nums[i]:
                count+=1
            if count >1:
                return False
            if nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1]=nums[i-2]
        return count<=1