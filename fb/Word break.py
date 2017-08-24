
class Solution(object):
    ## recursive
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: bool
    #     """
    #     # dict = set(wordDict)
    #     if wordDict == None:
    #         return False
    #     for idx,w in enumerate(wordDict):
    #         l = len(w)
    #         if len(w) == len(s):
    #             if s == w:
    #                 return True
    #
    #         if w == s[:l]:
    #             res = self.wordBreak(s[l:], wordDict[:idx]+wordDict[idx:])
    #             if res == True:
    #                 return True
    #
    #     return False

    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1, 1):
            for idx, w in enumerate(wordDict):
                l = len(w)
                if l <= i and s[i-l:i] == w and dp[-l+i]:
                    dp[i] = True
        return dp[-1]



sol = Solution()
s = 'cars'
w = ['car','car', 'rs']
res = sol.wordBreak(s, w)
print res

