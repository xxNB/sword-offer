class Solution:
    """
维持两个指针，慢的指针始终指向上一个非零数的后面，快指针向后扫描直至找到一个非零数，将快指针找到的非零数赋值给慢指针的位置后将慢指针后移一个位
置，同时将快指针所在处的数置为0。循环下去即可。
    """

    def moveZeros(self, nums):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            print(nums)
            fast += 1


c = Solution()
print(c.moveZeros([0, 1, 0, 3, 12]))
