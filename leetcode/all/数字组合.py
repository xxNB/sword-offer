class Solution(object):
    """
    回溯解法
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        self.result = []
        self.combination(candidates, target, [], 0)
        print( self.result)

    def combination(self, candidates, target, sublist, last):
        if target == 0:
            self.result.append(sublist[:])
        if target<candidates[0]:
            return
        for n in candidates:
            if n>target:
                return
            if n<last:
                continue
            sublist.append(n)
            self.combination(candidates, target-n, sublist,n)
            sublist.pop()


if __name__ == "__main__":
    Solution().combinationSum([2, 3, 6, 7], 7)