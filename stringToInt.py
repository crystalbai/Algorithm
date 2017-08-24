class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0
        res = 0; sign = 1
        for i in range(len(str)):
            if str[i] > '0' and str[i] < '9':
               res = res*10 + int(str[i])
            elif str[i] == '-':
                sign = -1
            else:
                continue

        return res * sign

sol = Solution()
res = sol.myAtoi('-12')
print res
