class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            alpha = [0 for i in range(26)]
            for c in s:
                i = ord(c)-ord('a')
                alpha[i]+=1
            
            for c in t:
                i = ord(c)-ord('a')
                alpha[i]-=1
                if alpha[i] < 0:
                    return False
            
            return True
        return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagramseen = set()
        # Iterate over the strs list
        for i in range(len(strs)):
            s = strs[i]
            if s in anagramseen:
                continue
            anagrams.append([s])
            for j in range(i+1, len(strs)):
                t = strs[j]
                # if t in anagramseen:
                #     continue
                if self.isAnagram(s, t):
                    k = len(anagrams) -1
                    anagrams[k].append(t)
                    anagramseen.add(t)
        
        return anagrams

