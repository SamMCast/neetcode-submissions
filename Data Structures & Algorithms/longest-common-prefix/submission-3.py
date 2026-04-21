class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)
        
        j = 0
        for i in range(len(shortest_str)):
            for word in strs:
                if shortest_str[i] != word[i]:
                    return shortest_str[:j]
            j+=1
        
        return shortest_str[:j]