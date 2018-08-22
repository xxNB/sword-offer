class Solution:
    def lenthOfLongestSubstring(self,s):
        res = 0
        if s is None or len(s) == 0:
            return res
        d = {}
        # tmp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                #记录非重复字符的起始位置,重复就往前推
                start = d[s[i]] +1
            tmp = i-start+1
            d[s[i]] = i
            res = max(res,tmp)
        return res