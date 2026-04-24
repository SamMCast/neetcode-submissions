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

        while idx < encoded_str_size:
            delimeter_idx = s.find(self.DELIMETER, idx)

            str_len = int(s[idx: delimeter_idx])
            str_start = delimeter_idx + 1
            str_end = str_start + str_len

            decoded_str = s[str_start:str_end]
            decoded_str_list.append(decoded_str)
            idx = str_end
        
        return decoded_str_list
        

            
