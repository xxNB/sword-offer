# -*- coding: utf-8 -*-

# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

class Soluition:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        string_list = [i for i in s]
        set_list = []
        for ix, word in enumerate(s):
            string_list.pop(ix)
            if word not in string_list:
                set_list.append(word)
            string_list = [i for i in s]
        return set_list[0]


c = Soluition()
print c.FirstNotRepeatingChar("")
