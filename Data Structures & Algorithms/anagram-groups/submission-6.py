'''
Sol 1: Sorting approach
Time Complexity: O(nmlogm) where n is the length of the string and m is longest word in the string
Space Complexity: O(n*m)
Intuition, two strings are consided anagrams if they are identical to each other. By sorting the strings we 
can determine which strings are anagrams of each other and then group them together using the sorted version
as key. Sorting strings is mlogm operation and considering there are n strings it together makes it O(nmlogm)
Space complexity would be O(n*m) because the output size matches the input size which is of O(n*m)
Sol 2: letter frequency table as a key
Time Complexity: Inutition a word is ana anagram of another word if the frequency of both words appear the exact amount of times.
Iterating through each word, we build a letter frequency table in O(nm) where is m is the longest word and n is
the size of the array. 
Space Complexity: We are generating a frequency table of size 26 n times with the final output matching the input
size so complexity would be O(nm) + O(n)
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