class Solution:
    '''
    count回文串
    time: O(n^2)
    space: O(1)
    '''
    def countSubstring(self,s):
        result =0
        if not s:
            return result
        length = len(s)
        for i in range(length):
            result+=self.count(s, i,i)
            result+=self.count(s,i,i+1)
        return result


    def count(self,s,beg, end):
        count =0
        while beg>=0 and end<len(s) and s[beg] == s[end]:
            count+=1
            beg-=1
            end+=1
        return count