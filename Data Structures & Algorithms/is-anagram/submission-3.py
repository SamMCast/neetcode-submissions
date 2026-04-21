class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # We can try an nlogn solution first
        # sorted_s = "".join(sorted(s))
        # sorted_t = "".join(sorted(t))
        # if sorted_s == sorted_t:
        #     return True
        # return False

        # We can try a linear solution
        alphabet = [0 for i in range(26)]
        for k in range(len(s)):
            i = ord(s[k]) - ord('a')
            j = ord(t[k]) - ord('a')
            alphabet[i]+=1
            alphabet[j]-=1

        for x in alphabet:
            if x != 0:
                return False
        return True

