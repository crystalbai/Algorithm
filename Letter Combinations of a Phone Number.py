class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if digits == '':
            return res
        s = d[digits[0]]
        if len(digits) > 1:
            str_prev = self.letterCombinations(digits[1:])
            for c in s:
                for str_single in str_prev:
                    res.append(c+str_single)
        else:
            for c in s:
                res.append(c)
        return res

sol = Solution()
res = sol.letterCombinations('23')
print res

