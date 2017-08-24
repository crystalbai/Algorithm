class TrieNode(object):
    def __init__(self):
        self.leave = False
        self.child = [None]*26


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) == 0:
            return self.root
        else:
            cur = self.root
            for i in range(len(word)):
                if cur.child[ord(word[i])-ord('a')] == None:
                    cur.child[ord(word[i])-ord('a')] = TrieNode()
                    cur = cur.child[ord(word[i])-ord('a')]
                else:
                    cur = cur.child[ord(word[i]) - ord('a')]
            cur.leave = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        return self.dfs(cur, word)

    def dfs(self, cur, word):
        if len(word) == 1:
            if word == '.':
                for v in cur.child:
                    if v != None:
                        if v.leave == True:
                            return True
                        else:
                            continue
                return False
            else:
                return cur.child[ord(word[0]) - ord('a')] != None and cur.child[ord(word[0]) - ord('a')].leave == True
        if word[0] != '.':
            if cur.child[ord(word[0]) - ord('a')] == None:
                return False
            else:
                return self.dfs(cur.child[ord(word[0]) - ord('a')], word[1:])
        else:
            tmp = False
            for j in range(26):
                if cur.child[j] != None:
                    tmp = tmp or self.dfs(cur.child[j], word[1:])
            return tmp

        # Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord('aaa')
obj.addWord('bad')
param_2 = obj.search('.ad')
print param_2