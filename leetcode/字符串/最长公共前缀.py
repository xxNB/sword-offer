class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs) == 0:
            return res

        temp = strs[0]
        for str in strs:
            if len(temp)>len(str):
                #找到最小字符串
                temp=str
        for i in range(0, len(temp)):
            for j in range(0, len(strs)):
                if strs[j][i] !=temp[i]:
                    return res
            res+=temp[i]
        return res