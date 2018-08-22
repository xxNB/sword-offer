class Solution:
    def findLongestPalindrome(self,s):
        """
        p[i,j] = p[i+1,j-1] if s[i]==s[j]
        p[i,j]=0 if s[i]!=s[j]
        :param s:
        :return:
        """
        length =len(s)
        maxlength = 0
        start=0
        p = [[False for _ in range(50)] for _ in range(50)]
        for i in range(length):
            p[i][i]=True
            if i < length-1and s[i]==s[i+1]:
                p[i][i+1]=True
                start=i
                maxlength=2
        for lens in range(3,length):
            for i in range(length-lens):
                j = i+lens-1
                if p[i+1][j-1] and s[i]==s[j]:
                    p[i][j]=True
                    maxlength=lens
                    start=i
        if maxlength>=2:
            return s[start,maxlength]
        return None