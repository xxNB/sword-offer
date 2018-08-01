class Solution:
    def groupAnagrams(self, strs):
        strs_map = {}
        result = []
        for str in strs:
            temp = "".join(sorted(str))
            if temp in strs_map:
                strs_map[temp].append(str)
            else:
                strs_map[temp] = [str]

        for str_list in strs_map.values():
            result.append(str_list)

        return result
