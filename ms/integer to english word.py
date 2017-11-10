class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def word(n):
            if n < 19:
                return to19[n-1]
            if n  < 100:
                return tens[n/10 -2] + to19[n%10]
            if n < 1000:
                return  [to19[n/100]] + ['Hundred'] + word(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return word(n/1000**p) + [w] + word(n%1000**p)
        return word(num)

sol = Solution()
print sol.numberToWords(12)