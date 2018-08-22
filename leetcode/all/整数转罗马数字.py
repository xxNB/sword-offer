class Solution:
    def inToRoman(self, num):
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        sb = []
        index = 0
        while num > 0:
            if num - ints[index] >= 0:
                num -= ints[index]
                sb.append(romans[index])
            else:
                index += 1
        return "".join(sb)
