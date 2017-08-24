class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dig = [0]*(len(num1)+len(num2)-1)
        res = ''
        if len(num1) == 0 or len(num2) == 0:
            return ''
        if num1 == '0' or num2 == '0':
            return '0'
        for idx1, i in enumerate(num1):
            for idx2, j in enumerate(num2):
                dig[idx1+idx2] = int(i)*int(j) + dig[idx1+idx2]
        add_tmp = 0
        for num in dig[::-1]:
            tmp_dig = (num + add_tmp)
            res = str(tmp_dig%10) +res
            add_tmp = tmp_dig/10
        if add_tmp != 0:
            res = str(add_tmp)+res

        return res

sol = Solution()
print sol.multiply('1234', '5678')







