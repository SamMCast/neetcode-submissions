class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_index = [0]*26
        runningCnt = len(s)
        for c in s:
            i = ord(c) - ord('a')
            alphabet_index[i]+=1
        
        for c in t:
            i = ord(c) - ord('a')
            if alphabet_index[i] == 0:
                return False
            alphabet_index[i]-=1
            runningCnt -=1

        return True



