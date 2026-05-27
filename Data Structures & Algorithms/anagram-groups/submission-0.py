class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        ssort = {}
        for x in strs:
            z = "".join(sorted(x))
            z = str(z)
            if z not in ssort:
                ssort[z] = [x]
            else:
                ssort[z].append(x)
        for x in ssort:
            ret.append(ssort[x])
        return ret
