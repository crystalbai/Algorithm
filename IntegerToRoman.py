from collections import OrderedDict
my_dictionary=OrderedDict()
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = OrderedDict([(1000,'M'), (900, 'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40, 'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')])
        res = ""
        while num > 0:
            for k in val:
                while num >= k:
                    res = res + val[k]
                    num -= k
        return res

sol = Solution()
res = sol.intToRoman(267)
print res


