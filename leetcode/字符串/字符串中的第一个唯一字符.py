class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for ix in range(len(s)):
            if s[ix] not in m:
                m[s[ix]] = 0
            m[s[ix]]+=1
            # else:
            #     m[s[i]]  = -1
            # print m
        for i in range(len(s)):
            if m[s[i]] == 0:
                return i
        return -1



c = Solution()
print(c.firstUniqChar("leetcode"))