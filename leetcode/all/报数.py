class Solution:
    def countAndSay(self, n):
        str = "1"
        for i in range(1,n):
            str = self.getStr(str)
        return str

    def getStr(self, tempstr):
        print(tempstr)
        cnt = 1
        res = ""
        for index, val in enumerate(tempstr):
            if index+1<len(tempstr) and val == tempstr[index+1]:
                cnt+=1
            else:
                res +=str(cnt)+val
                cnt =1
        return res


r = Solution()
print(r.countAndSay(4))