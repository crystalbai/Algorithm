class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        num = 0
        i = 0
        if len(s) == 0:
            return ''
        while s[i] >= '0' and s[i] <= '9':
            num = num * 10 + int(s[i])
            i+=1
        if num == 0:
            num = 1
        if s[i] == '[':
            c = 1
            j = i + 1
            while c != 0 and j < len(s):
                if s[j] == '[':
                    c += 1
                if s[j] == ']':
                    c -= 1
                j += 1
            return num * self.decodeString(s[i + 1:j - 1]) + self.decodeString(s[j:])
        tmp_str = ''
        while len(s)> i and s[i] >= 'a' and s[i] <= 'z' :
            tmp_str = tmp_str + s[i]
            i+=1
        return tmp_str + self.decodeString(s[i:])



sol = Solution()
print sol.decodeString("3[a2[c]]")