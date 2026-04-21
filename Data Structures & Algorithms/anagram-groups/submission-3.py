from collections import defaultdict
class Solution:
    def getAnagramTable(self, s: str) -> tuple[int]:
        alphabettable = [0]*26
        for c in s:
            i = ord(c) - ord('a')
            alphabettable[i]+=1
    
        return tuple(alphabettable)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramlist = defaultdict(list)

        for strwrd in strs:
            strwrdtable = self.getAnagramTable(strwrd)
            anagramlist[strwrdtable].append(strwrd)

        res = []
        for key, value in anagramlist.items():
            res.append(value)
        return res
            