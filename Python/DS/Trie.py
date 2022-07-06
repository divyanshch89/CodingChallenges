class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = dict()
class Trie:

    def __init__(self):
        #create a root trie node
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            node = current.children[c] if c in current.children else None
            if not node:
                #create a new trie node and update the dic for the current node
                node = TrieNode()
                current.children[c] = node
            current = node
        current.endOfWord= True
        

    def search(self, word: str) -> bool:
        #whole word should be present in the trie
        current = self.root
        for c in word:
            node = current.children[c] if c in current.children else None
            if not node:
                return False
            current = node
        return current.endOfWord
            
        

    def startsWith(self, prefix: str) -> bool:
        #search only the prefix
        current = self.root
        for c in prefix:
            node = current.children[c] if c in current.children else None
            if not node:
                return False
            current = node
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)