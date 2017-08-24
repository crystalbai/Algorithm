class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = max(len(a), len(b))
        if l == 0:
            return ''
        sign = 0
        ans = ''
        count = 1
        if len(a) <len(b):
            a,b = b,a
        for i in reversed(xrange(l)):
            if count > len(b):
                ans = str((sign + int(a[i])) % 2) + ans
                sign = (sign + int(a[i]))/2

            else:
                if int(a[i]) + int(b[-count])+sign == 2:
                    ans =  '0' + ans
                    sign = 1
                elif int(a[i]) + int(b[-count]) + sign == 3:
                    sign = 1
                    ans = '1' + ans
                elif int(a[i]) + int(b[-count])+ sign == 1:
                    sign = 0
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                    sign = 0

            count +=1
        if sign == 1:
            ans = '1' + ans
        return ans

sol = Solution()
ans = sol.addBinary("101111", '11')
print ans
