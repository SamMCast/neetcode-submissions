from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]

    # searches the word against the trie and returns the prefixlen
    def search(self, word: str, prefixlen: int) -> int:
        curr = self.root
        for i in range(prefixlen):
            c = word[i]
            if not c in curr.children:
                return i
            curr = curr.children[c]

        return prefixlen

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Let's find the shortest word in the list. This will be the word 
        # we will insert into the trie. THe longest common prefix is bounded
        # by the length of the word as in the longest common prefix can't exceed
        # the length of the word 
        min_indx = 0
        min_len = len(strs[0])
        for i,word in enumerate(strs):
            if len(word) < min_len:
                min_indx = i
                min_len = len(word)
        

        prefixTrie = Trie()
        prefixTrie.insert(strs[min_indx])
        prefixLen = min_len
        for word in strs:
            prefixLen = prefixTrie.search(word, prefixLen)
        
        return strs[0][:prefixLen]
        