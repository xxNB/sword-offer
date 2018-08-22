class Solution:
    def isPalindrome(self,s):
        if not s:
            return True
        left = 0
        right = len(s)-1
        while left<right:
            if not self.isAlphaNum(s[left]):
                left+=1
            elif not self.isAlphaNum(s[right]):
                right-=1
            elif s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True


    def isAlphaNum(self, ch):
        if 'a'<=ch<='z':
            return True
        if 'A'<=ch<='Z':
            return True
        if '0'<=ch<='9':
            return True
        return False

c=Solution()
print(c.isPalindrome("A man, a plan, a canal: Panama"))