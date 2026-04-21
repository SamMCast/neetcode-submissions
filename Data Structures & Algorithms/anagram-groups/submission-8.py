from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #Let's try an nslogs solution first
        # We will try the hash table solution
        '''
        so constructing an alphabet table is constant or O(26) and that will be done n times or O(n)
        appending incurs a cost of O(s) let's say that's the average size of the input string. Worst case 
        there are no anagrams so O(ns) for the entire array.
        '''
        for s in strs:
            freq = [0 for x in range(26)]
            for c in s:
                freq[ord(c) - ord('a')]+=1
            res[tuple(freq)].append(s)

        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     res[sorted_s].append(s)

        return list(res.values())
