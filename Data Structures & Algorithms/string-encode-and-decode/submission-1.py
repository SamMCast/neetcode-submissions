'''
The key to understanding this problem is knowing that encoding and decoding schemes rely on metada and they
have an agreed upon protocol. The metadata is usually the first thing that is read and decides how to either 
decode or encode in this case the string. I think it's much cleaner if for every string I specify the 
the len of the string followed by a pound sign followed by the string itself. The pound sign (#) is simply a 
delimeter so I can know when the string length begins and ends and where the string starts. 
'''
class Solution:
    DELIMETER = '#'
    def encode(self, strs: List[str]) -> str:
        encoded_str_list : list[str] = []
        for word in strs:
            encoded_str_list.append(str(len(word)) + self.DELIMETER + word)

        return "".join(encoded_str_list)

    
    

    def decode(self, s: str) -> List[str]:
        decoded_str_list : list[str] = []
        idx : int = 0
        encoded_str_size : int = len(s)

        def getStrlen_and_increment_idx_to_str(encoded_str: str):
            nonlocal idx
            startIdx: int = idx
            while idx < encoded_str_size and encoded_str[idx] != self.DELIMETER:
                idx+=1
            return int(encoded_str[startIdx:idx])

        while idx < encoded_str_size:
            wordLen = getStrlen_and_increment_idx_to_str(s)
            idx+=1
            decoded_str = s[idx:idx+wordLen]
            decoded_str_list.append(decoded_str)
            idx+=wordLen
        
        return decoded_str_list
        

            
