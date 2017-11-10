class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dig = [0] * (len(num1) + len(num2) - 1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                idx = len(num1) - 1 + len(num2) - 1 - i - j
                dig[idx] += int(num1[i]) * int(num2[j])
        carr = 0
        for idx, i in enumerate(dig):
            tmp = i + carr
            dig[idx] = str(tmp % 10)
            carr = tmp / 10
        while carr != 0:
            dig.append(str(carr % 10))
            carr = carr / 10
        dig.reverse()
        return ''.join(dig)
sol = Solution()
print sol.multiply('12','12')