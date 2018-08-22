class Solution:
    def privotIndex(self, nums):
        if not nums:
            return -1
        n = len(nums)
        i = -1
        j = n
        sum_l, sum_r = 0, 0
        while i < n - 1 and i < j and j > 0:
            print(sum_l, sum_r)
            print("i,j", i,j)
            if sum_l >=0 and sum_r >=0:
                if sum_r > sum_l:
                    i += 1
                    sum_l += nums[i]
                elif sum_r < sum_l:
                    j -= 1
                    sum_r += nums[j]
                elif sum_r == sum_l and i + 2 == j:
                    return i + 1
                elif j - i < 2:
                    return -1
                else:
                    i += 1
                    j -= 1
                    sum_l += nums[i]
                    sum_r += nums[j]
            else:
                if sum_r > sum_l:
                    j-= 1
                    sum_r += nums[j]
                elif sum_r < sum_l:
                    i+= 1
                    sum_l -= nums[i]
                elif sum_r == sum_l and i + 2 == j:
                    return i + 1
                elif j - i < 2:
                    return -1
                else:
                    i += 1
                    j -= 1
                    sum_l += nums[i]
                    sum_r += nums[j]


c = Solution()
print(c.privotIndex([-1,-1,-1,-1,-1,0]))


