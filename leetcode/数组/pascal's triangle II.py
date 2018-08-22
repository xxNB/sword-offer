class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        p = [1]
        if not rowIndex:
            return p
        for j in range(rowIndex):
            p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
        return p

