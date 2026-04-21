class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            alpha = [0 for i in range(26)]
            for c in s:
                i = ord(c) -ord('a')
                alpha[i] += 1

            for c in t:
                i = ord(c) -ord('a')
                alpha[i] -=1
                if alpha[i] < 0:
                    return False
            return True
        
        return False
        