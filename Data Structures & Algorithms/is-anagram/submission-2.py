class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_a = {}
        dict_b = {}
        for x in s:
            if x in dict_a:
                dict_a[x] = dict_a[x]+1
            else:
                dict_a[x] = 1
        for x in t:
            if x in dict_b:
                dict_b[x] = dict_b[x]+1
            else:
                dict_b[x] = 1
        return dict_a == dict_b
        
        