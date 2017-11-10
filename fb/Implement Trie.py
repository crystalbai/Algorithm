import collections
class TrieNode:
    def __init__(self):
        self.child = dict()
        self.is_word = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for l in word:
            if l not in cur.child:
                cur.child[l] = TrieNode()
            cur = cur.child[l]
        cur.is_word = True



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for l in word:
            if l not in cur.child:
                return False
            cur = cur.child[l]
        return cur.is_word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for l in prefix:
            if l not in cur.child:
                return False
            cur = cur.child[l]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
param_2 = obj.search('word')
print param_2
param_3 = obj.startsWith('wor')
print param_3