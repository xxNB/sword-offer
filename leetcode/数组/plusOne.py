class Solution:
    def plusone(self, digits):
        len_s = len(digits) - 1
        while len_s >= 0:
            if digits[len_s] == 9:
                digits[len_s] = 0
                if len_s == 0:
                    digits = [1] + digits
            else:
                digits[len_s] = digits[len_s] + 1
                break
            len_s -= 1
        return digits

c  =Solution()
c.plusone([1,9,9])