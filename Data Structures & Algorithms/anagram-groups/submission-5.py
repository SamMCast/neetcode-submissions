'''
Sol 1: Sorting approach
Time Complexity: O(nmlogm) where n is the length of the string and m is longest word in the string
Space Complexity: O(n*m)
Intuition, two strings are consided anagrams if they are identical to each other. By sorting the strings we 
can determine which strings are anagrams of each other and then group them together using the sorted version
as key. Sorting strings is mlogm operation and considering there are n strings it together makes it O(nmlogm)
Space complexity would be O(n*m) because the output size matches the input size which is of O(n*m)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freqTbl = [0]*26
            for c in s:
                freqTbl[ord(c)-ord('a')]+=1
            res[tuple(freqTbl)].append(s)

        return list(res.values())