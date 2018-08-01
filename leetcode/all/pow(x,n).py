"""
将幂不断除2，除到奇数时减1继续除，使得程序复杂度控制在O(logn)里
"""


class Solution:
    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1/x,-n)
        if n == 0:
            return 1
        if n == 2:
            return x*x
        return self.myPow(self.myPow(x,n/2),2) if not n%2 else x * self.myPow(self.myPow(x,n//2),2)


r = Solution()
print(r.myPow(2.0000, 13))
