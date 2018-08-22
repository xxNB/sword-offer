"""
给定一个字符串s
"""


class Solution:
    def __init__(self, string):
        self.string = string
        self.lens = len(self.string)

    #暴力枚举法
    def brute_force(self):
        maxcount = 0
        for j in range(self.lens):
            for k in range(j, self.lens):
                count = 0
                l,m = j,k
                while m>=l:
                    if self.string[1]==self.string[m]:
                        l,m = l+1, m-1
                    else:
                        break
                if m <l:
                    count = k-j +1
                if count > maxcount:
                    maxcount=count
        return maxcount

    # 枚举子串中心
    def brute_force_opti(self):
        maxcount = 0
        if self.lens == 1:
            return 1
        for j in range(self.lens-1): # 枚举中心
            count,u = 1, j
            for k in range(1, j+1):
                l,m = u+k, j-k
                if m>=0 &l<self.lens:
                    if self.string[l] == self.string[m]:
                        count+=2
                    else:
                        break
            if count > maxcount:
                maxcount = count
            if self.string[j] == self.string[j+1]:
                u,count = j+1,2
            for k in range(1,j+1):
                l,m = u+k, j-k
                if m>=0&l<self.lens:
                    if self.string[l]==self.string[m]:
                        count+=2
                    else:
                        break
            if count>maxcount:
                maxcount=count
        return maxcount
"""
manacher算法思想非常巧妙，首先遍历字符串，假设 i 为枚举中心，则 j (j<i) 为中心的最长回文子串长度发f[j] 便已经求出，此时 j 的影响范围便是[j-f[j]/2,j+f [j]] 。为了使左边的字符 j 对枚举中心右边的影响最大，需要使 j+f[j]/2 最大。找到满足j+f[j]/2最大的 j 之后，若 i 在[j,j+f[j]/2]中，则分两种情况：

1 . i 关于 j 对称的字符i'的影响范围完全包含在j的影响范围内，则由于回文性，i 的影响范围大于等于i'的影响范围，即f[i]>=f[i']

2. i 关于 j 对称的字符i'的影响范围不完全包含在j的影响范围内，此时i的右侧影响范围大于等于[j-f[j]/2,i']，即i+f[i]/2>=i'-j+f[j]/2

由于对称性，可得i+i" = 2*j。因此第一种情况下，f[i]>=f[2*j-i]；第二种情况下，f[i]>=f[j]+2*j-2*i。

综上1,2，可得f[i]>=min(f[2*j-i],f[j]+2*j-2*i)。由于i右边存在未遍历的字符，因此在此基础上，继续向两边扩展，直到找到最长的回文子串。

若i依然在j+f[j]/2后面，则表示i没有被前面的字符的影响，只能逐一的向两边扩展。

这个算法由于只需遍历一遍字符串，扩展的次数也是有限的，所以时间复杂度可以达到O（N）。
"""