class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        m = len(haystack)
        n = len(needle)
        if m<=n:return -1
        i = 0
        while i<m-n:
            j = 0
            while j <n:
                if haystack[i+j]!=needle[j]:
                    break
                j += 1
                if j==n:
                    return i
            i+=1
        return -1
c = Solution()
# print(c.strStr("mississippi"
# ,"issip"))

print(c.strStr("hello","ll"))