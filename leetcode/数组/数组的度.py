class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        既然要找出最短的子串使得其包含出现次数最多的元素，那么首先就是确定元素最多出现的次数，遍历一次就好了。接下来注意题目只要求包含任一出现
        次数最多元素的子串，所以对于有多个出现次数最多元素的情况，只要找到最短的、包含全部任一出现次数最多元素（抱歉这句话太绕）就好了。
        给定一个值，求包含全部与给定值相等的元素的最短子串该怎么求？其实很简单，记录下第一次出现和最后一次出现的位置就好了，两者相减就是最短长度，
        为什么？因为不会再有子串比它更短了（否则就是未包含全部元素）。对于有多个出现次数最多元素的情况，只需要找出这些元素的最短子串中最小的就好了。
        """
        counts = {}
        starts = {}
        ends = {}
        max_count = -float('inf')
        for i, num in enumerate(nums):
            if num not in starts:
                starts[num] = i
                counts[num] = 0
            counts[num]+=1
            ends[num] = i
            max_count = max(max_count, counts[num])
        reslut = float('inf')
        for num ,count in counts.items():
            if count == max_count:
                reslut = min(reslut, ends[num]-starts[num]+1)
        return reslut
