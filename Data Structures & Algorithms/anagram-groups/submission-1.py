class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tupList = []
        retVals = []
        tupDict = defaultdict(list)
        for x in strs:
            tupList = [0] * 26
            for y in x:
                tupList[ord(y) - ord('a')] += 1
            retVals.append((x, tupList))
        for x in retVals:
            indexTuple = str(x[1])
            tupDict[indexTuple].append(x[0])
        return list(tupDict.values())

        
            