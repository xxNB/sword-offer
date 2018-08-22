class Solution:
    def longestPalindrome(self,s):
        if not s or len(s)<1:
            return ''
        start,end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            len = max(len1,len2)
            if len>end-start:
                start = i-(len-1)/2
                end =i+len/2
        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L>=0 and R<len(s) and s[L]==s[R]:
            L-=1
            R+=1
        return R-L-1