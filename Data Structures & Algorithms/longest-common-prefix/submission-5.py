from collections import defaultdict
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_end_of_word = True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            self.insert(word)

        path_taken = []
        current_path = ""

        #1. Initialize the queue with the root
        queue = deque([self.root])

        #2. While are there nodes left to process
        while queue:
            lvl_size = len(queue)

            if lvl_size > 1:
                return "".join(path_taken)
            
            # 3. Process only the nodes at the current level
            for _ in range(lvl_size):
                node = queue.popleft() # pop from the front of the queue in O(1)
                path_taken.append(current_path)

                if node.is_end_of_word:
                    return "".join(path_taken)

                for path, child in node.children.items():
                    current_path = path
                    queue.append(child)
        
        return "".join(path_taken)
