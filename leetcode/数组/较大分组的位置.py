class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count = 1
        start = 0
        res = []
        c = S[0]
        for i in range(1, len(S)):
            if S[i] != c:
                if count > 2:
                    res.append([start, i - 1])
                count = 1
                start = i
            else:
                count += 1
            c = S[i]

        if count > 2:
            res.append([start, len(S) - 1])
        return res
