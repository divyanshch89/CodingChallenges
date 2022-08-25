#Link - https://leetcode.com/problems/search-suggestions-system/
'''
Approach1 -  Use Trie
Create a modified Trie (which also stores the whole number) and add all the words
Loop through the search word, append to a prefix and traverse the trie with the prefix and find top k suggestions
'''
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False
        self.word = ""

class Solution:
     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #all the products to a trie
        t = Trie()
        t.add_all(products)
        prefix = ''
        res = []
        for c in searchWord:
            prefix+=c
            res.append(t.get_top_k_elems(3,prefix,[]))
        return res

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def get_top_k_elems(self,k,prefix,ans):
        '''this is a modified version of startswith (prefix) logic of traditional trie'''
        current =self.root
        for c in prefix:
            node = current.children[ord(c)-ord('a')] if ord(c)-ord('a') in current.children else None
            if not node:
                #we dont have a valid result, return an empty list
                return []
            current = node
        self.dfs(current,k,ans)
        return ans        
    def dfs(self,node,k,ans):
        if len(ans)==k:
            return
        if node.EOW:
            ans.append(node.word)
        for c in node.children:
            self.dfs(c,k,ans)
        
    def add(self,word):
        current = self.root
        for c in word:
            node = current.children[ord(c)-ord('a')] if ord(c)-ord('a') in current.children else None
            if not node:
                current.children[ord(c)-ord('a')]=TrieNode()
            current = current.children[ord(c)-ord('a')]
        current.EOW=True
        #this will make sure that we can get the entire word or traversal path down the prefix tree
        current.word=word
    
    def add_all(self, words: List(str)):
        for word in words:
            self.add(word)
    
