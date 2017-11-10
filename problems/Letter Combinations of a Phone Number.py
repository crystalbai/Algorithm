class Solution(object):

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return res
        cur_s = list(d[digits[0]])

        for i in range(1, len(digits)):
            s = cur_s
            cur_s = []
            while len(s)!=0:
                node = s.pop(0)
                for s_n in list(d[digits[i]]):
                    cur_s.append(node+s_n)
        return cur_s

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return []
        cur = list(d[digits[0]])
        digits = digits[1:]
        while len(digits) != 0:
            cur_tmp = cur
            cur = []
            char = digits[0]
            digits = digits[1:]
            for l in list(d[char]):
                cur += [x+l for x in cur_tmp]
        return sorted(cur)
sol = Solution()
print sol.letterCombinations('2')