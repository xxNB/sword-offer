class Solution:
    """
    字符串长度为1：很明显，两个字符串必须完全相同才可以。
    字符串长度为2：当s1=”ab”, s2只有”ab”或者”ba”才可以。
    对于任意长度的字符串，我们可以把字符串s1分为a1,b1两个部分，s2分为a2,b2两个部分，满足（(a1~a2) && (b1~b2)）或者 （(a1~b2) && (a2~b1)）
    """

    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        l1 = list(s1)
        l2 = list(s2)
        # 将l1和l2排序，判断是否相等
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[length - i:]) and self.isScramble(s1[i:], s2[:length - i]):
                return True
        return False
