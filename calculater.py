class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        d = 0
        sign = '+'
        i = 0
        s =s.strip(' ')
        while i < len(s):
            if s[i] == ' ':
                i+=1
                if i>= len(s):
                    break

            if s[i] >= '0' and s[i] <= '9':
                d = d * 10 + int(s[i])
            if not (s[i] >= '0' and s[i] <= '9' ) or i == len(s) -1:
                if sign == '+':
                    st.append(d)
                    d = 0
                if sign == '-':
                    st.append(-d)
                    d = 0
                if sign == '*':
                    pre = st.pop()
                    st.append(d * pre)
                if sign == '/':
                    pre = st.pop()
                    st.append(pre/d)
                if s[i]!=' ':
                    sign = s[i]
                    d = 0
            i+=1
        res = 0
        while len(st) != 0:
            res = res + st.pop()
        return res


sol = Solution()
print sol.calculate("3+5 / 2 ")