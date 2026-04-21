class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for word in strs:
            encoded_str = str(len(word)) + "#" + word
            encoded_list.append(encoded_str)
        encoded = "".join(encoded_list)
        return encoded

    def decode(self, s: str) -> List[str]:
        wrdLst = []
        i = 0
        while i < len (s):
            j = i
            while s[j] != "#":
                j+=1
            wrdLn = int(s[i:j])
            j+=1
            i = j+ wrdLn
            wrdLst.append(s[j:i])
        return wrdLst

