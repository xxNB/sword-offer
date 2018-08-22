class Solution:
    def longestCommonPrefix(self,strs):
        if strs is None or len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            tmp =res
            res = ''
            for j in range(min(len(strs[i]), len(tmp))):
                if tmp[j] == strs[i][j]:
                    res += tmp[j]
                else:
                    break
        return res



r = Solution()
print(r.longestCommonPrefix(["flowers","floders","fliders"]))