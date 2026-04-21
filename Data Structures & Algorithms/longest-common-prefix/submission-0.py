"""
I need to find the shortest word in the array. I can then use the size of the
shortest word to determine how long I should iterate for. Let's say the 
shortest word is 3, I would iterate until the count 3. That would be an outer loop
in the inner loop, I would be comparing the index of each word to each other until
I'm either able to complete a pass of the total amount of words in the array or
or until a letter doesn't match. If all the letters match, I will move on to the
next count. This has a time complexity of O(ns) where n is the total amount of words
in the array and s is the shortest word in the array. 
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        minsize = len(strs[0])

        for i in range(1, len(strs)):
            minsize = min(len(strs[i]), minsize)
        
        prefix_str = []
        for j in range(minsize):
            for k in range(len(strs)-1):
                if strs[k][j] != strs[k+1][j]:
                    res = "".join(prefix_str)
                    return res
            prefix_str.append(strs[0][j])

        res = "".join(prefix_str)
        return res 