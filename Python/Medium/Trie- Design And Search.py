#Link -  https://leetcode.com/problems/design-add-and-search-words-data-structure/

from lib2to3.pytree import Node


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.eow =  False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            node = current.children if c in current.children else None
            if not node:
                node =  TrieNode()
                current.children[c] = node
            current = node
        current.eow = True
        

    def search_helper(self,word,node,index):
        if len(word)==index:
            #the whole world len was traversed
            return node.eow
        if word[index]!='.':
            return node.children[word[index]] and self.search_helper(word,node.children[word[index]], index+1)
        else:
            #traverse all the children of current node and see for any child node path to rest of the world exist
            for n in node.children.keys():
                if node.children[n] and self.search_helper(word,node.children[n],index+1):
                    return True
        return False


    def search(self, word: str) -> bool:
        '''
        Case 1: when there is no '.' is present
        Case 2: when . is present in the word
        '''
        return self.search_helper(word,self.root,0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)