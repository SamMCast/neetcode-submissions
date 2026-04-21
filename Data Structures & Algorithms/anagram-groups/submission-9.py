from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagrams = defaultdict(list)

        for word in strs:
            let_cnt = [0 for x in range(26)]
            for c in word:
                let_cnt[ord(c) - ord('a')]+=1
            
            Anagrams[tuple(let_cnt)].append(word)

        return list(Anagrams.values())
        
            
